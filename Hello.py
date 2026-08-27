# This is my first Python programming assignment
# Author: Alexey Konovalov
# Date: 25.08.2026


name = input("What is your name? ")
print("Hello,", name)

my_id = 1403427

print(f"Integer padded: {my_id:08d}")
print(f"Two decimals: {my_id:.2f}")
print(f"Binary: {my_id:b}")
print(f"Hexadecimal: {my_id:#x}")

first = my_id // 1000000
print("First digit:", first)

last = my_id % 10
print("Last digit:", last)

result = first + last
print("Result:", result)