import os, sys, json, io, signal

last = ""

sys.stdout = io.TextIOWrapper(
    open(sys.stdout.fileno(), "wb", buffering=0),
    write_through=True
)

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

def write(flush=False, *args):
    sys.stdout.write(" ".join([str(item) for item in args]))
    if flush: sys.stdout.flush()

def clear(by=""):
    write(True, "\033[2J\033[3J\033[H" + str(by))

def blit(*layers):
    grids = [layer.split("\n") for layer in layers]
    base = grids[0]

    for grid in grids[1:]:
        for row_i, row in enumerate(grid):
            if row_i >= len(base):
                base.append(row)
                continue

            base_row = list(base[row_i])
            for col_i, ch in enumerate(row):
                if ch != " ":
                    if col_i < len(base_row):
                        base_row[col_i] = ch
                    else:
                        base_row.append(ch)
            base[row_i] = "".join(base_row)

    return "\n".join(base)

def render(frame):
    global last

    if frame != last:
        clear(frame)
        last = frame

def container(width, height, y=1):
    tx, ty = termsize()
    
    top = ("+" + "-"*width + "+").center(tx)
    row = ("|" + " "*width + "|").center(tx)
    
    c = "\n"*y + top
    c += ("\n" + row) * height
    c += "\n" + top

    return c

def pos(content, x, y):
    content = content.splitlines()
    for i, v in enumerate(content):
        content[i] = " "*x + v
    return "\n"*y + "".join(content)

def init():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def ls(dc):
    c = ""
    for i, v in dc.items():
        c += str(v["prefix"]) + str(v["value"]) + (str(("/" + v["max"])) if v["max"] != -1 else "") + str(v["suffix"])
    return c