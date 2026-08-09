# idle game or something
import os, time, sys

def logo():
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(scriptPath, "logo.txt")
    with open(path, "r") as file:
        return file.read()

def getchar():
    #this is so confusing
    if os.name == "nt": #means its windows
        import msvcrt
        ch = msvcrt.getch()
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
        "\x1b[C": "RIGHT", "\x1b[D": "LEFT"}.get(char, char)

def clear():
    print("\033[H\033[J", end="")

def start(splash):
    entries = ["play", "options", "quit"]
    selected = 0
    while True:
        clear()
        if splash: print(splash)
        for i in entries:
            print(f"  {"▐" if selected == entries.index(i) else " "} {i}")
        match getchar().lower():
            case "up" | "w": selected -= 1 if selected > 0 else 0
            case "down" | "s": selected += 1 if selected < len(entries) - 1 else 0
            case _: pass
                

start(logo())
while True:
    print(f"pressed: {getchar()}")