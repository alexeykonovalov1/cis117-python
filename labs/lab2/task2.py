# Lab 2 task 2
# Group # 1 7
# Author: Alexey Konovalov
# Date: 10/03/2026


def isogram(text):
    """isogram: a word in which no letter of the alphabet occurs more than once"""
    length = len(text)

    for i in range(length):
        for j in range(i + 1, length):
            if text[i].lower() == text[j].lower():
                return False

    return True


print(isogram("demographics"))
print(isogram("hello"))