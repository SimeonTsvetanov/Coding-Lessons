"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#4

SUPyF Dictionaries - 05. Mixed Phones

Problem:
You will be given several phone entries, in the form of strings in format:
{firstElement} : {secondElement}
The first element is usually the person’s name, and the second one – his phone number.
The phone number consists ONLY of digits, while the person’s name can consist of any ASCII characters.
Sometimes the phone operator gets distracted by the Minesweeper she plays all day, and gives you first the phone,
and then the name. e.g. : 0888888888 : Pesho. You must store them correctly, even in those cases.
When you receive the command “Over”, you are to print all names you’ve stored with their phones.
The names must be printed in alphabetical order.
Examples:

Input:
14284124 : Alex
Gosho : 088423123
Ivan : 412048192
123123123 : Nanyo
Pesho : 150925812
Over

Output:
Alex -> 14284124
Gosho -> 88423123
Ivan -> 412048192
Nanyo -> 123123123
Pesho -> 150925812
"""
phonebook = {}

while True:
    command = [item for item in input().split(" : ")]
    if "Over" in command:
        break
    if command[1].isdigit():
        phonebook[command[0]] = command[1]
    else:
        phonebook[command[1]] = command[0]

for name, number in sorted(phonebook.items()):
    print(f"{name} -> {number}")



