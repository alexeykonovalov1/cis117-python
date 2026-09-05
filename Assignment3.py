# This is my Python programming Homework 3
# Author: Alexey Konovalov
# Date: 05.09.2026


highway_num = int(input("Enter the highway number: "))

if 1 <= highway_num <= 99:
    if highway_num % 2 == 0:
        print(f"Highway {highway_num} is a primary east/west highway.")
    else:
        print(f"Highway {highway_num} is a primary north/south highway.")

if 100 <= highway_num <= 999:
    last_digit = highway_num % 100
    if highway_num % 2 == 0:
        print(f"Interstate {highway_num} is an auxiliary highway serving I-{last_digit}, which runs east/west.")
    else:
        print(f"Interstate {highway_num} is an auxiliary highway serving I-{last_digit}, which runs north/south.")

if highway_num <= 0 or highway_num > 999:
    print("Invalid highway number.")