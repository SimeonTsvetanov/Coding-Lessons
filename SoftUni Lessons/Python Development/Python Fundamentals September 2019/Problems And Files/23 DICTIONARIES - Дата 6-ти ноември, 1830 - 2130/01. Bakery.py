"""
Dictionaries - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1736#0

SUPyF2 Dictionaries-Lab - 01. Bakery

Problem:
This is your first task in your new job.
You were tasked to create a list of the stock in a bakery and you really don't want to fail at you first day at work.
You will receive a single line containing some food (keys) and quantities (values).
They will be separated by a single space (the first element is the key, the second – the value and so on).
Create a dictionary with all the keys and values and print it on the console

Examples:
Input:                              	Output:
bread 10 butter 4 sugar 9 jam 12	    {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
"""

string_to_list = [item for item in input().split()]

bakery = {}

for key in range(0, len(string_to_list), 2):
    item = string_to_list[key]
    value = int(string_to_list[key + 1])
    bakery[item] = value

print(bakery)

