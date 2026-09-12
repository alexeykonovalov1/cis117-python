# This is Homework 4 Task 2
# Author: Alexey Konovalov
# Date: 11.09.2026


#loop
while True:
    input_year = int(input("Enter a year (or a negative number to exit): "))

# loop break
    if input_year < 0:
        print("Program ended.")
        break

# leap year check
    if (input_year % 400 == 0) or (input_year % 4 == 0 and input_year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year.")