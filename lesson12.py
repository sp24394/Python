items = {
    "croissant": {"price": 2.99, "stock": 2},
    "small mac": {"price": 3.17,"stock": 7},
    "big mac": {"price": 849.99,"stock": 1},
    "1 grape": {"price": 7.99,"stock": 2}
}
info = "\tstock view\n\tstock update <item_name> <add/set> <qty>\n\tbuy <item_name> <qty>\n\thelp\n\tquit"
print(f"\n{info}\n\n")

def listget(list, index):
    return list[index] if index < len(list) else None
def tryfloat(x):
    try:
        return float(x)
    except:
        return 0.0

while True:
    inp = input("\t\t>")
    command = inp.lower().split(" ")
    if not listget(command, 0): print(f"\tunknown command '{inp}'")
    else:
        match command[0]:
            case "stock":
                if not listget(command, 1): print(f"\tunknown command '{inp}'")
                else:
                    if command[1] == "view":
                        tot = 0
                        for x in items:
                            print(f"\n\t{x}:\n\t\tprice: ${items[x]["price"]:.2f}\n\t\tstock: {items[x]["stock"]}\n\t\tvalue: ${(items[x]["price"]*items[x]["stock"]):.2f}")
                            tot += items[x]["price"]*items[x]["stock"]
                        print(f"\n\ttotal value: ${tot:.2f}\n")
                    elif command[1] == "update":
                        if not listget(command, 2) or not listget(command, 3) or not listget(command, 4): print(f"\tunknown command '{inp}'")
                        else:
                            command[2] = command[2].replace("_", " ")
                            if not items.get(command[2]):
                                print(f"\tunknown item '{command[2]}'")
                            else:
                                old = items[command[2]]["stock"]
                                if command[3] == "add":
                                    items[command[2]]["stock"] = old + round(tryfloat(command[4]))
                                elif command[3] == "set":
                                    items[command[2]]["stock"] = round(tryfloat(command[4]))
                                if not command[3] == "set" and not command[3] == "add":
                                    print(f"\tunknown argument '{command[3]}'")
                                else:
                                    print(f"\t{command[2]}: {old} -> {old + round(tryfloat(command[4]))}")
            case "help":
                print(f"\n{info}\n\n")
            case "buy":
                if not listget(command, 1) or not listget(command, 2): print(f"\tunknown command '{inp}'")
                else:
                    command[1] = command[1].replace("_", " ")
                    if not items.get(command[1]):
                        print(f"\tunknown item '{command[1]}'")
                    else:
                        if round(tryfloat(command[2])) > items[command[1]]["stock"]:
                            print("\tnot enough stock")
                        else:
                            old = items[command[1]]["stock"]
                            items[command[1]]["stock"] -= round(tryfloat(command[2]))
                            print(f"\t${(items[command[1]]["price"]*round(tryfloat(command[2]))):.2f}\n\t{command[1]}: {old} -> {old - round(tryfloat(command[2]))}")
            case "quit":
                print("\n"); break
            case _:
                print(f"\tunknown command '{inp}'")