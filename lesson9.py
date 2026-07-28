def caeser(text, shift):
    new = ""
    for char in text:
        new = new + chr(ord(char) + shift)
    return new

print(caeser(input("Text: "), 3))