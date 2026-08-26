#3
#2
#1
#Liftoff!

def sum_to(n):
   if n <= 1:
       return n
   return n + sum_to(n - 1)

def fib(n):
   if n <= 1:
       return n
   return fib(n - 1) + fib(n - 2)

#1, 1, 3, 5, 9, 15


def best(x, coins, memo=None):
    if memo is None:
        memo = {}

    if x == 0:
        return 0
    if x < 0:
        return float('inf')
    if x in memo:
        return memo[x]

    fewest = float('inf')
    for c in coins:
        fewest = min(fewest, 1 + best(x - c, coins, memo))

    memo[x] = fewest
    return fewest

print(best(6, [1, 3, 4]))