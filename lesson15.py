import math

def largest(n, m):
    return n if n > m else m

def circle_area(r):
    return math.pi*r**2

def longest_word(sentence):
    word = ""
    for i in sentence.split(" "):
        if len(i) > len(word): word = i
    return word

def factorial(n):
    return math.factorial(n)

def is_prime(n):
    if n == 1: return False
    elif n == 2: return True
    elif not n % 2: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True
    # ngl i didnt know how to do this faster one but i
    # dont really feel like coding a brute force one rn

for i in [1, 2, 5, 7, 31, 13, 24, 25]:
    if is_prime(i): print(i)