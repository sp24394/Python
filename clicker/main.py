# idle game or something
import os, time, sys

def logo():
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(scriptPath, "logo.txt")
    with open(path, "r") as file:
        return file.read()

def getchar():
    if os.name == "nt":
        import msvcrt
        return msvcrt.getch().decode("utf-8", errors="ignore")
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

def clear():
    print("\033[H\033[J", end="")

def start(splash, showmenu):
    clear()
    if splash: print(splash)
    if showmenu:
        print("  ↵ play\n    quit")

start(logo(), True)