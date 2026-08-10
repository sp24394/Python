import util as u, art, time

u.init()

data = {
    "credits": {
        "prefix": "",
        "suffix": "c",
        "value": 10,
        "max": -1
    }
}

u.clear()
lastsize = None

while True:
    size = u.termsize()
    if size != lastsize:
        lastsize = size
        tx, ty = size
        ty = max(ty, 16)
    u.render(u.blit(u.container(tx - 8, ty - 4), u.pos(u.ls(data), 5, 2)))