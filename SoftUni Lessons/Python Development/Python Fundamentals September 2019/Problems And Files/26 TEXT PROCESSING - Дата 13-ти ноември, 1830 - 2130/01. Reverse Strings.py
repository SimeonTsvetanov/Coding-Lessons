"""
Text Processing - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1739#0

SUPyF2 Text-Processing-Lab - 01. Reverse Strings

Problem:
You will be given series of strings until you receive an "end" command.
Write a program that reverses strings and prints each pair on separate line in format "{word} = {reversed word}".

Examples:
|------------|---------------------|
|  Input:    |   Output:           |
|------------|---------------------|
|  helLo     |   helLo = oLleh     |
|  Softuni   |   Softuni = inutfoS |
|  bottle    |   bottle = elttob   |
|  end       |                     |
|------------|---------------------|
|  Dog       |   Dog = goD         |
|  caT       |   caT = Tac         |
|  chAir     |   chAir = riAhc     |
|  enD       |                     |
|------------|---------------------|
"""
# Solution #1:
"""
while True:
    word = input()
    if word == "end":
        break
    print(f"{word} = {word[::-1]}")
"""
# Solution #2:
"""
while True:
    word = input()
    if word == "end":
        break
    reverse_word = ""
    for letter in reversed(word):
        reverse_word += letter
    print(f"{word} = {reverse_word}")
"""
# Solution #3
while True:
    word = input()
    if word == "end":
        break
    print(f"{word} = {''.join(reversed(word))}")
