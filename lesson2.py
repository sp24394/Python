item, qty, price = "Breakin' 2: Electric Boogaloo", 378, 19.98
print(f"""\n\t|{"":^42}|
\t|{"thanks for buying mmovie":^42}|
\t|{"":^42}|
\t|  ======================================  |
\t|{"":^42}|
\t|  {item:<40}|
\t|    $/unit: ${round(price, 2):<{34-len(str(price))}}|
\t|    QTY: {qty:<33}|
\t|{"":^42}|
\t|  TOTAL: ${round(price*qty, 2):<{50-len(str(price*qty))}}|
\t|{"":^42}|""")