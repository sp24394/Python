def clear(w):
    print(f"\033[H\033[J{w}", end="")

c = 0
tc = 0
while True:
    c += 1
    tc += 1
    clear(f"uwu x{c}")