"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#0

SUPyF2 D.Types and Vars Exercise - 01. Integer Operations
Problem:
Read four integer numbers.
Add first to the second, divide (integer) the sum by the third number and multiply the result by the fourth number.
Print the result.

Examples:
Input: Output:
10     30
20
3
3

Input: Output:
15     42
14
2
3
"""
print(int(((int(input()) + int(input())) // int(input())) * int(input())))
