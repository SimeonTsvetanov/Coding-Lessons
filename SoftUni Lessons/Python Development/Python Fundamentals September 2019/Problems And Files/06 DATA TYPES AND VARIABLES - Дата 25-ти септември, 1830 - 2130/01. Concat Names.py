"""
Data Types and Variables - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1721#0
Video: https://www.youtube.com/watch?v=i2vHypjJkB4

SUPyF2 D.Types and Vars Lab - 01. Concat Names

Problem:
Read two names and a delimiter. Print the names joined by the delimiter.
Examples:

Input:
John
Smith
->
Output:
John->Smith

Input:
Jan
White
<->
Output:
Jan<->White

Input:
Linda
Terry
=>
Output:
Linda=>Terry
"""

first_name, second_name, delimiter = input(), input(), input()
print(f"{first_name}{delimiter}{second_name}")

