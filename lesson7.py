import math
shape = input("Triangle, rectangle, or circle: ").lower()

if shape == "triangle":
    bs = float(input("Base: "))
    h = float(input("Height: "))
    a = float(input("Side A: "))
    b = float(input("Side B: "))
    c = float(input("Side C: "))
    print(f"Perimeter: {a+b+c}\nArea: {bs*h/2}")

elif shape == "rectangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    print(f"Perimeter: {(b+h)*2}\nArea: {b*h}")

elif shape == "circle":
    r = float(input("Radius: "))
    print(f"Circumference: {2 * math.pi * r}\nArea: {math.pi * r**2}")