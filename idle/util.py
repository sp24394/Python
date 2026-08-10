import os, sys, json

last = ""

# 0: black, 1: red, 2: green, 3: yellow,
# 4: blue, 5: magenta, 6: cyan, 7: white

def tc(v):
    return f"\033[{v+30}m"

def bg(v):
    return f"\033[{v+40}m"

def bold():
    return f"\033[1m"

def reset():
    return f"\033[0m"

def termsize():
    size = os.get_terminal_size()
    return size.columns, size.lines

def getchar():
    if os.name == "nt":
        import msvcrt
        ch = msvcrt.getch()

        if ch == b"\r":
            return "ENTER"
        
        if ch in (b"\x00", b"\xe0"):
            code = msvcrt.getch()
            return {b"H": "UP", b"P": "DOWN",
                    b"K": "LEFT", b"M": "RIGHT"}.get(code, "")
        
        return ch.decode("utf-8", errors="ignore")

    else:
        import tty, termios, select
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = os.read(fd, 1).decode("utf-8", errors="ignore")

            if ch == "\x1b":
                if select.select([fd], [], [], 0.01)[0]:
                    char += sys.stdin.read(2)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return {"\x1b": "ESC", "\x1b[A": "UP", "\x1b[B": "DOWN",
        "\x1b[C": "RIGHT", "\x1b[D": "LEFT", "\r": "ENTER"}.get(ch, ch)

def write(*args):
    sys.stdout.write(" ".join([str(item) for item in args]))
    sys.stdout.flush()

def clear(by=""):
    write("\033[2J\033[3J\033[H" + str(by))

def blit(*layers):
    base = list(layers[0])
    for layer in layers[1:]:
        for i, ch in enumerate(layer):
            if ch != " ":
                if i < len(base):
                    base[i] = ch
                else:
                    base.append(ch)
    return "".join(base)

def render(frame):
    clear(frame)
    last = frame

def container(width, height, y=1):
    tx, ty = termsize()
    c = "\n"*y + ("+" + "-"*(width) + "+").center(tx)
    c += ("\n" + ("|" + " "*(width) + "|").center(tx))*height
    c += "\n"*y + ("+" + "-"*(width) + "+").center(tx)

    return c