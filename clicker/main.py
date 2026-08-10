# idle game or something
import os, time, sys, json; from datetime import datetime, date; from pathlib import Path

scriptPath = os.path.dirname(os.path.abspath(__file__))
savepath = Path(scriptPath) / "saves"

save = "testsave"

def savefiles():
    return [p for p in savepath.glob("*.json") if p.is_file()]

def savesmenu():
    entries = savefiles()
    entries.append("create a new save +")
    chosen = menu(entries, " choose a save file +~\n")
    if chosen != "create a new save +":
        save = chosen
    else:
        success = False
        clear()
        inp = input(" name your save slot +~\n  ▌↲ save name: ")
        if inp.isalnum(): success = True
        while not success:
            clear()
            inp = input(" alpha-numeric characters only +~\n  ▌↲ save name: ")
            if inp.isalnum(): success = True
        clear()

def readsave(save):
    with open(Path(savepath) / f"{save}.json", "r") as save:
        return json.load(save)

def writesave(save, newdata):
    savedata = readsave().update(newdata)
    with open(Path(savepath) / f"{save}.json", "w") as save:
        json.dump(savedata, save, indent=2)

def logo():
    path = Path(scriptPath) / "logo.txt"
    with open(path, "r") as file:
        return file.read()

def getchar():
    #this is so confusing
    if os.name == "nt": #means its windows
        import msvcrt
        ch = msvcrt.getch()
        if ch == b"\r":
            return "ENTER"
        if ch in (b"\x00", b"\xe0"): #esc keu thingy
            code = msvcrt.getch()
            return {b"H": "UP", b"P": "DOWN", b"K": "LEFT", b"M": "RIGHT"}.get(code, "")
        return ch.decode("utf-8", errors="ignore")
    else: #any other os
        import tty, termios, select
        fd = sys.stdin.fileno() #linux uses integers to
        #identify open files so u access it with that
        #instead of the file as an object
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = os.read(fd, 1).decode("utf-8", errors="ignore")
            if char == "\x1b":
                #check if theres more bytes in queue cus
                #the prefix is the same code as esc so
                #wait for 10ms to see if theres more (arrows)
                if select.select([fd], [], [], 0.01)[0]:
                    char += sys.stdin.read(2)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return {"\x1b": "ESC", "\x1b[A": "UP", "\x1b[B": "DOWN",
        "\x1b[C": "RIGHT", "\x1b[D": "LEFT", "\r": "ENTER"}.get(char, char)

def clear():
    print("\033[H\033[J", end="")

def menu(entries, prefix="", suffix=""):
    selected = 0
    while True:
        clear()
        print(prefix, end="")
        for i in entries:
            print(f"  {"▌↲" if selected == entries.index(i) else " "} {i}")
        print(suffix, end="")
        character = getchar()
        match character.lower():
            case "up" | "w":
                if selected > 0: selected -= 1
                else: selected = len(entries) - 1
            case "down" | "s":
                if selected < len(entries) - 1: selected += 1
                else: selected = 0
            case "enter":
                return entries[selected]
            case _: pass

def splash(icon):
    clear(); print(icon)

clear()
savesmenu()