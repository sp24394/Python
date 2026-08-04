rates = {
    "USD": 0.59,
    "AUD": 0.92,
    "GBP": 0.47,
    "EUR": 0.55,
    "JPY": 88.50,
    "FJD": 1.34
}
while True:
    value = float(input("NZD to convert: "))
    rate = rates.get(input("Convert to: ").upper())
    print(f"{"Invalid values" if not value or not rate else (value * rate):.2f}")
    if input("Convert again? Y/n").lower() == "n": break