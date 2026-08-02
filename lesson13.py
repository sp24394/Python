from turtle import *

bob = Turtle()
bob.speed(10)

def shape(sides=4, size=400, colour="black", fill=False, fcolour="black"):
    pp, pf = bob.color()
    bob.color(colour, fcolour)

    if fill: bob.begin_fill()
    for i in range(sides):
        bob.forward(size/sides)
        bob.left(360/sides)
    if fill: bob.end_fill()

    bob.color(pp, pf)

shape(16, 300, "blue", True, "red")

mainloop()