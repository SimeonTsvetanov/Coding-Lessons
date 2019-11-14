"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#0

SUPyF2 Lists Basics Lab - 01. Courses

Problem:
You will receive a single number n. On the next n lines you will receive names of courses.
You have to create a list of them and print it.

Example:
Input:
2
PB Python
BF Python
Output:
['PB Python', 'PF Python']

Input:
4
Front-End
C# Web
JS Core
Programming Fundamentals
Output:
['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']
"""
my_list = []

for line in range(int(input())):
    my_list += [input()]

print(my_list)

