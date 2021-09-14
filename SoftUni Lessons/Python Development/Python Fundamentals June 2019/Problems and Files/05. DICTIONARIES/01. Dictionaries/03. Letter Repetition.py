"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#2

SUPyF Dictionaries - 03. Letter Repetition

Problem:
You will be given a single string, containing random ASCII character.
Your task is to print every character, and how many times it has been used in the string.

Examples:
-----------------------------------------------------------------
Input:                                                  Output:
aaabbaaabbbccc                                          a -> 6
                                                        b -> 5
                                                        c -> 3
-----------------------------------------------------------------
"""
letters_input = [item for item in input()]

letter_repetition = {}

for letter in letters_input:
    if letter not in letter_repetition:
        letter_repetition[letter] = letters_input.count(letter)

for key, value in letter_repetition.items():
    print(f"{key} -> {value}")

    
def redo_solution():
    list_letters = [i for i in input()]

    letters = {}

    for j in list_letters:
        if j not in letters.keys():
            letters[j] = list_letters.count(j)

    for letter, count in letters.items():
        print(f"{letter} -> {count}")


# redo_solution()
