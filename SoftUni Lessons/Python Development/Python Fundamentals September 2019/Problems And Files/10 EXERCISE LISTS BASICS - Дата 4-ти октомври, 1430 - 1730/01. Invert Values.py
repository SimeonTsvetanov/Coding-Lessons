"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#0

SUPyF2 Lists Basics Exercise - 01. Invert Values

Problem:
Write a program that receives a single string containing numbers separated by a single space.
Print a list containing the opposite of each number
Example
Input	        Output
1 2 -3 -3 5	    [-1, -2, 3, 3, -5]
-4 0 2 57 -101	[4, 0, -2, -57, 101]
"""
print([abs(int(digit)) if int(digit) < 0 else -abs(int(digit)) for digit in input().split(" ")])


