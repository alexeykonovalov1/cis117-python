# Lab 2 task 1
# Group # 1 7
# Author: Alexey Konovalov
# Date: 10/03/2026

def tautogram(text):
    """tautogram: a text in which all words start with the same letter """
    words = text.split()
    
    first_letter = words[0][0].lower()
    
    for word in words:
        if word[0].lower() != first_letter:
            return False
    
    return True
print(tautogram("Big bears bite berries"))
print(tautogram("Big bears eat berries"))