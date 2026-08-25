# This is my first Python programming assignment
# Author: Alexey Konovalov
# Date: 25.08.2026

name = input("What is your name? ")
print("Hello,", name)

my_id = "01403427"
print("My ID:", my_id)

my_id_number = int(my_id)
print("Decimal:", my_id_number)
print("Binary:", f"{my_id_number:b}")
print("Hexadecimal:", f"{my_id_number:#x}")

first = int(my_id_number) // 10000000
print("First digit:", first)

last = int(my_id_number) % 10
print("Last digit:", last)

result = first + last
print("Result:", result)