import random, time, sys

tests = []
start = 4
multiplier = 4
limit = 16777217
status = 0

while True:
    start *= multiplier
    tests.append(start)
    if start > limit:
        break

def start_test(rule, num_tests):
    global status
    start_time = time.perf_counter()
    true_tests = 0

    for i in range(num_tests):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        t = False
        status += 1

        match rule:
            case 1:
                t = x == 5 or y == 5
            case 2:
                t = not x % 2 and not y % 2
            case 3:
                t = x + y == 8

        if t:
            true_tests += 1

    exec_time = time.perf_counter() - start_time
    return true_tests, num_tests, exec_time

rule = int(input("Enter rule (1, 2, or 3): "))
rules = [
    "roll 2 dice, check if either one rolled a 5",
    "roll 2 dice, check if both are even",
    "roll 2 dice, check if both add to 8"
]
summaries = []

st = time.perf_counter()

for num_tests in tests:
    true_tests, total, exec_time = start_test(rule, num_tests)
    summaries.append((total, true_tests / total, exec_time))

print(f"TEST {rule} RESULTS ({rules[rule-1]}):")
for total, ratio, exec_time in summaries:
    print(f"- {total} rolls:")
    print(f"  - true ratio: {ratio:.6f}")
    print(f"  - percent true: {(ratio*100):.2f}%")
    print(f"  - exec time: {exec_time:.4f}s")

print(f"total time: {time.perf_counter() - st}s")