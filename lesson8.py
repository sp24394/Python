word = "Hello Goodbye"
print(f"{word[0:5]}")
print(f"{word[len(word)-3:len(word)].capitalize()}")
print(f"{word[6:10]}")
print(f"{word[3:8].lower()}")
print(f"{word[::2][0:len(word[::2])-1]}")
print(f"{word[::-1]}")