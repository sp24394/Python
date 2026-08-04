balance = 300 
if input("PIN: ") != "1234": print("Access denied") 
else: 
    inp = float(input("Withdrawal amount: $")) 
    if inp > 500: print("Withdrawal limit exceeded.") 
    elif inp > balance: print("Insufficient funds.") 
    else: balance -= inp; print("Withdrawal successful!") 