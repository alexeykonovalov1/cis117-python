# This is my chaos theory practice Python programming file.
# Author: Alexey Konovalov
# Date: 26.09.2026

def next_value(x):
    return 4 * x * (1 - x)


steps = int(input("How many steps? "))
first = float(input("Enter a starting value between 0 and 1: "))
second = first + 0.000001

max_difference = 0

for step in range(1, steps + 1):
    first = next_value(first)
    second = next_value(second)

    difference = abs(first - second)
    if difference > max_difference:
        max_difference = difference
    print(f"Step {step}: difference = {difference:.8f}")
print(f"highest difference = {max_difference:.8f}")