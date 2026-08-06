def get(t, i):
    try: return t[i]
    except: return None

def main():
    contacts = {}

    while True:
        cmd = input(" >").split(" ")
        match get(cmd, 0):
            case "add":
                if get(cmd, 1) and get(cmd, 2):
                    contacts[get(cmd, 1)] = get(cmd, 2)
            case "view":
                for i in contacts:
                    print(i + ":\t  " + str(contacts.get(i)))
            case "search":
                if get(cmd, 1):
                    for i in contacts:
                        if get(cmd, 1) in i:
                            print(i + ":\t  " + contacts.get(i))
            case "delete":
                if get(cmd, 1):
                    try:
                        del contacts[get(cmd, 1)]
                    except:
                        print("Not in contacts")
            case "exit":
                break
            case _:
                print("Unknown command")


main()