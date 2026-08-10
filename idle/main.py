import util as u, art, time

u.clear()
lastsize = None

while True:
    size = u.termsize()
    if size != lastsize:
        lastsize = size
        tx, ty = size
        u.render(u.blit(u.container(tx - 8, ty - 4)))