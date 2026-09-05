# This is my sixth Python programming practice file.
# Author: Alexey Konovalov
# Date: 28.08.2026


percentage = float(input("What is the tip percentage? "))
num_people = int(input("How many people are splitting the bill? "))
bill_amount = float(input("What is the total bill amount? "))

total_amount = bill_amount + (bill_amount * percentage / 100)

tip_amount = total_amount - bill_amount

tip_per_person = tip_amount / num_people

total_per_person = total_amount / num_people

print()

print("Tip percentage: " + str(percentage) + "%")
print("Number of people: " + str(num_people))
print("Bill amount: " + str(bill_amount))

print()

print("Tip amount: " + str(round(tip_amount, 2)))
print("Tip per person: " + str(round(tip_per_person, 2)))
print("Total amount: " + str(round(total_amount, 2)))
print("Total per person: " + str(round(total_per_person, 2)))

print()

