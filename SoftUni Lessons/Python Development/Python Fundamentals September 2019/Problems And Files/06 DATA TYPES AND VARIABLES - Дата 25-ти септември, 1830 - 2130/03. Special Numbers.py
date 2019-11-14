"""
Data Types and Variables - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1721#2
Video: https://www.youtube.com/watch?v=i2vHypjJkB4

SUPyF2 D.Types and Vars Lab - 03. Special Numbers

Problem:
A number is special when its sum of digits is 5, 7 or 11.
Write a program to read an integer n and for all numbers in the range 1…n to print the number and if it is special or not (True / False).
Input:
15
Output:
1 -> False
2 -> False
3 -> False
4 -> False
5 -> True
6 -> False
7 -> True
8 -> False
9 -> False
10 -> False
11 -> False
12 -> False
13 -> False
14 -> True
15 -> False
"""

n = int(input())
for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
