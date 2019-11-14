"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#1

SUPyF2 Lists Basics Exercise - 02. Multiples List

Problem:
Write a program that receives two numbers (factor and count)
and creates a list with length of the given count and contains only elements that are multiples of the given factor.

Example:
Input	Output
2
5	    [2, 4, 6, 8, 10]

1
10	    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
factor = int(input())
count = int(input())
my_list = []
digit = 1
while True:
    if len(my_list) == count:
        break
    if digit % factor == 0:
        my_list += [digit]
    digit += 1
print(my_list)


