# This is my first self pracctice Python programming file.
# Author: Alexey Konovalov
# Date: 25.09.2026


import random

choices = {1: "Paper", 2: "Scissors", 3: "Rock"}

while True:

    answer = input("Do you wanna play now? ").lower().strip()

    if answer not in ["y", "yes", "ye", "yeah"]:
        print("See ya!")
        continue

    user_choice = int(input("Pick between 1, 2, or 3: "))

    if user_choice in choices:
        print(f"Wise choice! You picked {choices[user_choice]}")
    else:
        print("Choice is incorrect")
        continue

    comp_choice = random.randint(1, 3)

    print(f"Computer choice is {choices[comp_choice]}")

    if user_choice == comp_choice:
        print("Tie")

    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
        print("You win")

    else:
        print("You lose")