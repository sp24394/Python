age = float(input("Age: "))//1
base = 12 if age < 16 else 17.5
discount = 0
while True:
    promo_code = input("Promo code: ") or None
    match promo_code:
        case "student" | "senior":
            if (promo_code == "student" and age > 18) or (promo_code == "senior" and age < 65): print(f"Promo code '{promo_code}' cannot be applied at your age.")
            else: discount = 0.15; break
        case "free":
            discount = 1; break
        case None:
            break
        case _:
            print(f"Code '{promo_code}' not found.\nYou can just press enter if you don't have a code.\n")
if discount != 0: print(f"Applied a {discount*100}% discount. (${base:.2f} > ${(base*(1-discount)):.2f})")
print(f"Total: ${(base*(1-discount)):.2f}")