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
    pass

def get_cost():
    pass

def view_cart():
    pass

def remove_item(item, qty):
    pass

def update_item(item, price, qty):
    pass