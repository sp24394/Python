# idle game or something
import os, time
    #TODO read logo.txt
def logo():
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(scriptPath, "logo.txt")
    with open(path, "r") as file:
        return file.read().split("\n&&\n")

def clear():
    print("\033[H\033[J", end="")

def start():
    anim = logo()
    for i in anim:
        clear()
        print(i)
        time.sleep(0.2/len(anim))


start()