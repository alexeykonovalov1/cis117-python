# This is my second self practice Python programming file.
# Author: Alexey Konovalov
# Date: 26.09.2026

import random


def open_chest():
    num_opens = int(input("How many times do you wanna open the chest? "))

    while num_opens <= 0:
        print("Please enter a positive number.")
        num_opens = int(input("How many times do you wanna open the chest? "))

    choices = ["Gold", "Spiders", "Crown"]
    score = 0
    gold_count = 0
    spider_count = 0
    crown_count = 0

    for opening in range(num_opens):
        prize = random.choice(choices)

        if prize == "Gold":
            score += 10
            gold_count += 1
        elif prize == "Spiders":
            score -= 5
            spider_count += 1
        else:
            score += 25
            crown_count += 1

        print(f"Chest {opening + 1}: {prize}. Score: {score}")

    print(f"Total score: {score}")
    print(f"Gold: {gold_count}, Spiders: {spider_count}, Crowns: {crown_count}")
    print(f"Percentage of Gold: {gold_count / num_opens * 100:.2f}%")
    print(f"Percentage of Spiders: {spider_count / num_opens * 100:.2f}%")
    print(f"Percentage of Crowns: {crown_count / num_opens * 100:.2f}%")


open_chest()