# This is my third self practice Python programming file.
# Author: Alexey Konovalov
# Date: 17.10.2026

# How many times does a certain digit appear in the count to the given number?


def count_digit_occurrences(initial_number, digit_to_count):
    count = 0
    for number in range(0, initial_number + 1):
        count += str(number).count(str(digit_to_count))

    return count


def main():
    initial_number = int(input("Enter a number: "))
    while initial_number < 0:
        print("Please enter a non-negative number.")
        initial_number = int(input("Enter a number: "))

    digit_to_count = int(input("Enter a digit to count (0-9): "))
    while digit_to_count < 0 or digit_to_count > 9:
        print("Please enter a valid digit (0-9).")
        digit_to_count = int(input("Enter a digit to count (0-9): "))

    count = count_digit_occurrences(initial_number, digit_to_count)
    print(f"The digit {digit_to_count} appears {count} times in the numbers from 0 to {initial_number}.")


if __name__ == "__main__":
    main()
