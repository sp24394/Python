import sys, os, time, random; from colorama import Fore, Back, Style
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"; import pygame.mixer

_base = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.init()
pygame.mixer.set_num_channels(24)

# good speeds:
#   undertale - 1
#   animalese - 0.45

def speak(text, speed = 1, soundfont = None, mods = "", pause = True):
    text = str(text)
    if soundfont == "." or soundfont == "/": soundfont = ""

    if soundfont:
        directory = os.path.join(_base, "sounds", soundfont)
        if not os.path.exists(directory):
            speak(f"\tSoundfont '", 1, "default", f"{Fore.BLACK}{Back.RED}", False)
            speak(soundfont, 1, "default", f"{Fore.BLACK}{Back.RED}{Style.BRIGHT}", False)
            speak(f"' doesn't exist. Available soundfonts:", 1, "default", f"{Fore.BLACK}{Back.RED}")
            time.sleep(0.3)
            for i in sorted(os.listdir(os.path.join(_base, "sounds"))):
                sys.stdout.write("\n\t ")
                pygame.mixer.Sound(os.path.join(_base, "sounds", "default_alt", "0.wav")).play()
                speak(f"- '{i}'", 4, None, f"{Fore.BLACK}{Back.RED}{Style.BRIGHT}", False)
            time.sleep(0.2)
            return

        soundfont_is_abc = False
        if os.path.exists(os.path.join(directory, ".abc")):
            soundfont_is_abc = True

        if soundfont_is_abc:
            sounds = {}
            for i in os.listdir(directory):
                if i != ".abc":
                    sounds[i.replace(".wav", "").lower()] = pygame.mixer.Sound(os.path.join(directory, i))
        else:
            sounds = []
            for i in os.listdir(directory):
                sounds.append(pygame.mixer.Sound(os.path.join(directory, i)))

    blacklist = [
        "\n",
        "\t"
    ]
    
    sys.stdout.write(mods)
    sys.stdout.flush()

    for i in range(len(text)):
        skip = False
        if i >= len(text):
            break

        if text[i] == "|":
            skip = True
            time.sleep(0.2)

        if skip:
            skip = False
        else:
            sys.stdout.write(text[i])
            sys.stdout.flush()
            if soundfont and not text[i].lower() in blacklist:
                if not soundfont_is_abc:
                    if len(sounds) == 1:
                        current_sound = sounds[0]
                        current_sound.play()
                    else:
                        current_sound = random.choice(sounds)
                        current_sound.play()
                else:
                    if text[i].lower() in sounds:
                        current_sound = sounds[text[i].lower()]
                        current_sound.play()

            if not text[i].lower() in blacklist and i < len(text)-1:
                time.sleep((1/30)/speed)
        
    if mods: sys.stdout.write(Style.RESET_ALL); sys.stdout.flush()
    if soundfont and pause and current_sound: time.sleep(current_sound.get_length() + 0.05)


v = "swkbd_futsu"
while True:
    speak(f"The quick brown fox jumps over the lazy dog.", 1, v, f"{Fore.WHITE}{Back.BLUE}")
    sys.stdout.write(f"\nSoundfonts: {sorted(os.listdir(os.path.join(_base, "sounds")))}\n")
    v = input("Pick a new soundfont: ")