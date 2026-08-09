# idle game or something
import os, time
    #TODO read logo.txt
def logo():
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(scriptPath, "logo.txt")
    with open(path, "r") as file:
        return file.read()

def clear():
    print("\033[H\033[J", end="")

def start(splash, showmenu):
    clear()
    if splash: print(splash)
    if showmenu:
        print("  > play\n    quit")

start(logo(), True)