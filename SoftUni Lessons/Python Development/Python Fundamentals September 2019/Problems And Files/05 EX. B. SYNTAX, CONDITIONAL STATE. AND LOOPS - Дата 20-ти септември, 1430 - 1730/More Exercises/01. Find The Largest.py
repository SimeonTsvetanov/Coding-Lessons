"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1720#0
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise More - 01. Find The Largest

Problem:
Given a number, print the largest number that can be formed from the digits of the number given.
Examples:
Input:	Output:
213	    321
7389	9873
"""
number = [int(digit) for digit in input()]
number.sort(reverse=True)
print("".join([str(num) for num in number]))

