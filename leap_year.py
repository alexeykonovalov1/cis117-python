# This is Homework 4
# Author: Alexey Konovalov
# Date: 11.09.2026


input_year = int(input("Enter a year: "))

if (input_year % 400 == 0) or (input_year % 4 == 0 and input_year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year.")