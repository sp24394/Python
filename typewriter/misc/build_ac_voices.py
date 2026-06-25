"""Build Animal Crossing voice folders under sounds/ from the raw files in voices/.

Kana characters: map English letters to best-fit Japanese syllable substitutes.
Swkbd characters: use literal English Alph_Eng letters + Digit_Eng numbers.
"""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOICES = os.path.join(ROOT, "voices")
SOUNDS = os.path.join(ROOT, "sounds")

# ---- kana characters (main Voice_<Char>_Kana_<syllable>.wav) ----
KANA_CHARS = ["Aneki", "Bonyari", "Futsu", "Genki", "Ghost",
              "Hakihaki", "Kiza", "Kowai", "Otona"]

# preference list per English letter; first available syllable wins.
# PRIORITY: make it sound like the letter's NAME when reciting the alphabet
# (a="ay", b="bee", ...). Where no syllable is close to the name, fall back to
# the plain phonetic pick. Trailing entries are fallbacks for sparse voices.
LETTER_PREFS = {
    "a": ["e", "a"],                        # "ay"  -> e (eh)
    "b": ["bi", "bu", "be", "ba", "bo"],    # "bee" -> bi
    "c": ["si", "su", "se", "sa", "so"],    # "see" -> si (shi)
    "d": ["di", "du", "de", "da", "do"],    # "dee" -> di
    "e": ["i", "e"],                        # "ee"  -> i
    "f": ["fa", "fe", "fo", "fi"],          # "ef"  -> no CV match, keep fa
    "g": ["zi", "gu", "ge", "gi", "ga", "go"],  # "gee"/"jee" -> zi (ji)
    "h": ["ha", "he", "ho", "hi", "hu"],    # "aitch" -> no CV match, keep ha
    "i": ["a"],                             # "eye" -> a (ah onset)
    "j": ["je", "ju", "ja", "jo"],          # "jay" -> je
    "k": ["ke", "ku", "ka", "ki", "ko"],    # "kay" -> ke
    "l": ["ru", "ra", "ro", "re", "ri"],    # "el"  -> no CV match, keep ru
    "m": ["mu", "ma", "mo", "me", "mi", "n"],   # "em" -> keep mu; ghost -> n
    "n": ["n", "nu", "na", "no"],           # "en"  -> n
    "o": ["o"],                             # "oh"  -> o
    "p": ["pi", "pu", "pe", "pa", "po"],    # "pee" -> pi
    "q": ["kyu", "ku", "kwa", "ka"],        # "cue" -> kyu
    "r": ["ru", "ra", "ro", "re", "ri"],    # "ar"  -> no CV match, keep ru
    "s": ["su", "sa", "so", "se", "si"],    # "es"  -> no CV match, keep su
    "t": ["ti", "tu", "te", "ta", "to"],    # "tee" -> ti
    "u": ["yu", "u"],                       # "you" -> yu
    "v": ["bi", "bu", "be", "ba", "bo"],    # "vee" -> bi (no v in JP)
    "w": ["wa", "wo", "wi", "we"],          # "double-u" -> no match, keep wa
    "x": ["ku", "su", "ki"],                # "ecks" -> no CV match, keep ku
    "y": ["wa", "ya", "yu", "yo", "ye"],    # "why" -> wa
    "z": ["zi", "zu", "ze", "za", "zo"],    # "zee" -> zi
}

# ---- swkbd characters (literal English) ----
SWKBD_CHARS = ["Bonyari", "Futsu"]
# digit language fallback order (Eng target; closest-sounding European next)
DIGIT_LANGS = ["Eng", "Ger", "Frc", "Spn", "Itl", "Por", "Jpn", "Rus", "Dut"]


def kana_inventory(char):
    prefix = f"Voice_{char}_Kana_"
    inv = {}
    for f in os.listdir(VOICES):
        if f.startswith(prefix) and f.endswith(".wav") and "KanaEx" not in f:
            syl = f[len(prefix):-4]
            inv[syl] = f
    return inv


def make_folder(name):
    path = os.path.join(SOUNDS, name)
    os.makedirs(path, exist_ok=True)
    open(os.path.join(path, ".abc"), "w").close()
    return path


def main():
    report = []

    # kana characters
    for char in KANA_CHARS:
        inv = kana_inventory(char)
        folder = make_folder(char.lower())
        used = {}
        missing = []
        for letter, prefs in LETTER_PREFS.items():
            chosen = next((s for s in prefs if s in inv), None)
            if chosen is None:
                missing.append(letter)
                continue
            shutil.copyfile(os.path.join(VOICES, inv[chosen]),
                            os.path.join(folder, f"{letter}.wav"))
            used[letter] = chosen
        report.append((char.lower(), len(used), used, missing, []))

    # swkbd characters
    for char in SWKBD_CHARS:
        folder = make_folder(f"swkbd_{char.lower()}")
        used = {}
        missing = []
        digit_notes = []
        # letters: literal Alph_Eng_<UPPER>
        for i in range(26):
            letter = chr(ord("a") + i)
            src = os.path.join(VOICES, f"Voice_Swkbd_{char}_Alph_Eng_{letter.upper()}.wav")
            if os.path.exists(src):
                shutil.copyfile(src, os.path.join(folder, f"{letter}.wav"))
                used[letter] = f"Eng_{letter.upper()}"
            else:
                missing.append(letter)
        # digits 0-9, Eng preferred, fall back across languages
        for d in range(10):
            chosen_lang = None
            for lang in DIGIT_LANGS:
                src = os.path.join(VOICES, f"Voice_Swkbd_{char}_Digit_{lang}_{d}.wav")
                if os.path.exists(src):
                    shutil.copyfile(src, os.path.join(folder, f"{d}.wav"))
                    chosen_lang = lang
                    break
            if chosen_lang is None:
                missing.append(str(d))
            elif chosen_lang != "Eng":
                digit_notes.append(f"{d}<-{chosen_lang}")
        report.append((f"swkbd_{char.lower()}", len(used) + (10 - sum(
            1 for d in range(10) if str(d) in missing)), used, missing, digit_notes))

    # print summary
    for name, count, used, missing, notes in report:
        print(f"\n## {name}  ({count} files + .abc)")
        if used and name.startswith("swkbd"):
            print("   letters: literal English A-Z")
        elif used:
            print("   " + "  ".join(f"{k}->{v}" for k, v in used.items()))
        if notes:
            print("   digit fallbacks: " + ", ".join(notes))
        if missing:
            print("   MISSING (no good match): " + ", ".join(missing))


if __name__ == "__main__":
    main()
