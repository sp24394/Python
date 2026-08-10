import util as u, time

u.clear()

while True:
    tx, ty = u.termsize()
    u.render(u.blit(u.container(tx - 8, ty - 4)))
    time.sleep(0.01)