import sys, time
from colorama import init, Fore, Back, Style

multipliers = {
    ",": 0.2,
    ".": 0.11
}

def speak(text, speed = 1, mods = ""):
    text = str(text)

    sys.stdout.write(mods)
    sys.stdout.flush()

    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        if i < len(text) and not text[i] == " ": time.sleep((0.03/multipliers.get(text[i], 1))/speed)
    
    if mods: sys.stdout.write(Style.RESET_ALL); sys.stdout.flush()

speak(f"Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 1, f"{Fore.WHITE}{Back.BLUE}")