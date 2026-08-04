import sys, time
t = "pineapples"
while True:
    for i in range(len(t)):
        sys.stdout.write(f"\r{" "*i}{t[i]}{" "*(len(t)-i)}")
        time.sleep(0.05)
    for i in range(len(t)):
        sys.stdout.write(f"\r{" "*(len(t)-i-1)}{t[len(t)-i-2]}{" "*i}")
        time.sleep(0.05)