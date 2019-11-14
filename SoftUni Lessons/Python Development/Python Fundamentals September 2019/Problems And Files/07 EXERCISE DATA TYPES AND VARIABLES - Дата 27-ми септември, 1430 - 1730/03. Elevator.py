"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#2

SUPyF2 D.Types and Vars Exercise - 03. Elevator

Problem:
Calculate how many courses will be needed to elevate n persons by using an elevator of capacity of p persons.
The input holds two lines: the number of people n and the capacity p of the elevator.

Examples:
Input: Output:
17
3	   6
Input: Output:
4
5	   1
Input: Output:
10
5	   2
"""
import math
print(math.ceil(int(input()) / int(input())))

