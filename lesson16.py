"""
def slice(x):
    return x.lower().split("@")
"""

"""
import random

def generate_number():
    return random.randint(0,100)

def get_guess():
    return round(float(input("Choose a number: ")))

def check_guess(n, g):
    return "more" if n > g else "less" if g > n else True

def main():
    n = generate_number()
    while True:
        r = check_guess(n, get_guess())
        print("Higher!" if r == "more" else "Lower!" if r == "less" else "Correct!")
        if r == True: break

main()
"""

board = [0,0,0,0,0,0,0,0,0]

def print_board(b):
    c = 0
    for i in b:
        c += 1
        print(" " + str(i), end=" |" if c%3 else "\n")
        if not c % 3 and not c == 9: print("---+---+---")

def check_winner(b):
    pass

def move(b, p):
    pass

def main():
    pass

print_board(board)