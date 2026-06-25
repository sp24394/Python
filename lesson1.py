import sys

types = [
    "noun",
    "verb",
    "noun",
    "place",
    "verb"
]
words = []

for i in range(len(types)):
    words.append(input(f"Type a {types[i]}: "))

sys.stdout.write(f"The {words[0]} {words[1]} the {words[2]} at {words[3]} while {words[4]}ing.")