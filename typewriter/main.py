import sys, os, time, random; from colorama import Fore, Back, Style
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"; import pygame.mixer

_base = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.init()
pygame.mixer.set_num_channels(24)

def speak(text, speed = 1, soundfont = None, mods = "", pause = True):
    text = str(text)

    if soundfont:
        directory = os.path.join(_base, "sounds", soundfont)
        if not os.path.exists(directory):
            speak(f"\tSoundfont '", 1, "default", f"{Fore.BLACK}{Back.RED}", False)
            speak(soundfont, 1, "default", f"{Fore.BLACK}{Back.RED}{Style.BRIGHT}", False)
            speak(f"' doesn't exist. Available soundfonts:", 1, "default", f"{Fore.BLACK}{Back.RED}")
            time.sleep(0.3)
            for i in os.listdir(os.path.join(_base, "sounds")):
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

    multipliers = {
    ",": 0.2,
    ".": 0.11
    }

    blacklist = [
        "\n",
        "\t"
    ]
    
    sys.stdout.write(mods)
    sys.stdout.flush()

    for i in range(len(text)):
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

        if not text[i].lower() in blacklist and i < len(text)-1 and multipliers.get(text[i], True) != None:
            time.sleep(((1/30)/multipliers.get(text[i], 1))/speed)
    
    if mods: sys.stdout.write(Style.RESET_ALL); sys.stdout.flush()
    if soundfont and pause and current_sound: time.sleep(current_sound.get_length() + 0.05)


speak(f"Hello, world!", 0.6, "asriel", f"{Fore.WHITE}{Back.BLUE}")