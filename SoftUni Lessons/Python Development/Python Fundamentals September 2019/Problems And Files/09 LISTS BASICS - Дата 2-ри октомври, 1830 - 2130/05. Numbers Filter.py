"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#4

SUPyF2 Lists Basics Lab - 05. Numbers Filter

Problem:
You will receive a single number n. On the next n lines you will receive integers.
After that you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive). Finally, print the result.

Example:
Input:
5
33
19
-2
18
998
even
Output:
[19, -2, 18, 998]

Input:
3
111
-4
0
negative
Output:
[-4]
"""
even = []
odd = []
negative = []
positive = []

for how_many_times in range(int(input())):
    digit = int(input())
    if digit % 2 == 0:
        even += [digit]
    else:
        odd += [digit]
    if digit < 0:
        negative += [digit]
    else:
        positive += [digit]
print(eval(input()))
