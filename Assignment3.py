# This is Homework 3
# Author: Alexey Konovalov
# Date: 05.09.2026

# added loop
while True:
    highway_num = int(input("Enter the highway number (or 0 to exit): "))

# loop break
    if highway_num == 0:
        print("Program ended.")
        break

    if 1 <= highway_num <= 99:
        if highway_num % 2 == 0:
            print(f"Interstate {highway_num} is a primary east/west highway.")
        else:
            print(f"Interstate {highway_num} is a primary north/south highway.")

    elif 100 <= highway_num <= 999:
        last_digit = highway_num % 100
        if highway_num % 2 == 0:
            print(f"Interstate {highway_num} is an auxiliary highway serving I-{last_digit}, which runs east/west.")
        else:
            print(f"Interstate {highway_num} is an auxiliary highway serving I-{last_digit}, which runs north/south.")

    else:
        print("Invalid highway number.")