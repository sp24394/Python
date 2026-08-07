# idle game or something
import os
    #TODO read logo.txt
def logo():
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(scriptPath, "logo.txt")

def clear():
    print("\033[H\033[J", end="")

def start():
    clear()
    print(logo())

start()