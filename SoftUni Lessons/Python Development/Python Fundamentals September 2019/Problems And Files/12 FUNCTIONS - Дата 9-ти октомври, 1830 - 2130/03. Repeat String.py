"""
Functions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1727#2

SUPyF2 Functions-Lab - 03. Repeat String

Problem:
Write a function that receives a string and a repeat count n.
The function should return a new string (the old one repeated n times).

Examples:
Input:	    Output:

abc
3	        abcabcabc

String
2	        StringString
"""


def repeat(string, times):
    return string * times


print(repeat(input(), int(input())))
