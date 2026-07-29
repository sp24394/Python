items = {
    "croissant": {"price": 2.99, "stock": 2},
    "poop sock": {"price": 3.17,"stock": 7},
    "super poop sock": {"price": 849.99,"stock": 1},
    "1 grape": {"price": 7.99,"stock": 2}
}
info = "\tstock view\n\tstock update <item_name> <add/set> <qty>\n\tbuy <item_name> <qty>\n\thelp\n\tquit"
print(f"\n{info}\n\n")
while True:
    command = input("\t\t>").lower().split(" ")
    match command[0]:
        case "stock":
            if command[1] == "view":
                print(items)
            elif command[1] == "update":
                old = items[command[2]]["stock"]
                if command[3] == "add":
                    items[command[2]]["stock"] = old + round(float(command[4]))
                elif command[3] == "set":
                    items[command[2]]["stock"] = round(float(command[4]))
                print(f"\t{command[2]}: {old} -> {old + round(float(command[4]))}")
        case "help":
            print(f"\n{info}\n\n")
        case "buy":
            old = items[command[1]]["stock"]
            items[command[1]]["stock"] -= round(float(command[2]))
            print(f"\t${items[command[1]]["price"]*round(float(command[2]))}\n\t{command[1]}: {old} -> {old - round(float(command[2]))}")