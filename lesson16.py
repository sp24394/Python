from colorama import Fore, Back, Style; from pynput import keyboard

board = [0,0,0,0,0,0,0,0,0]
turn = 1

def clear():
    print("\033[H\033[J", end="")

def player(n, t = True):
    return f"{Fore.RED}{Style.BRIGHT}X" + (Style.RESET_ALL if t else "") if n == 1 else f"{Fore.BLUE}{Style.BRIGHT}O" + (Style.RESET_ALL if t else "")

def print_board(b, e=False):
    c = 0
    global turn
    for i in b:
        c += 1
        print(" " + ((Style.DIM + str(c) + Style.RESET_ALL) if i == 0 else player(i)), end=" |" if c%3 else "\n")
        if not c % 3 and not c == 9: print("---+---+---")
    if e: print(f"\n{player(turn, False)}'s turn.{Style.RESET_ALL}\nChoose a position: ", end="")

def check_winner(b):
    full = True
    win = 0
    for i in b:
        if i == 0: full = False
        else:
            pass # TODO STUFF HERE
    
    if full:
        clear()
        print_board(b)
    
    return win

def on_press(key):
    pass

def on_release(key):
    global turn
    if key == keyboard.Key.esc:
        clear()
        return False

    try:
        pos = int(key.char)-1
        if board[pos] == 0:
            board[pos] = turn
            turn = 1 if turn == 2 else 2
        win = check_winner(board)
        if win == 0: clear(); print_board(board, True)
        else:
            clear()
            print_board(board)
            print(f"\n{player(turn, False)} wins!" if win != 3 else "\nDraw!")
            return False
    except Exception as e:
        clear(); print_board(board, True)
        return

clear()
print_board(board, True)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()