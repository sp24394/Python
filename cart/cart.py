import json; from pathlib import Path

DIR = Path(__file__).resolve().parent
CART_FILE = DIR/"cart.json"

def read_cart():
    with open(CART_FILE, "r") as file:
        return json.load(file)

def write_cart(content):
    with open(CART_FILE, "w") as file:
        json.dump(content, file, indent=2)


try:
    read_cart()
except:
    write_cart({})
cart = read_cart()


def add_item(item, cost, qty):
    item = item.lower()
    cart.update({item: {"cost": cost, "qty": (cart.get(item).get("qty") if cart.get(item) else 0) + qty}})

def get_cost():
    c = 0
    for i, v in cart.items():
        c += v.get("cost") * v.get("qty")
    return c

def view_cart():
    for i in cart:
        print(i)
        for v, v2 in cart.get(i).items():
            print(f" - {v}: {v2}")
        print("")

def remove_item(item, qty):
    pass

def update_item(item, price, qty):
    pass

view_cart()