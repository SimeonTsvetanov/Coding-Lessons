"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#1

SUPyF2 Functions-Exercise - 02. Add and Subtract

Problem:
You will receive three integer numbers.
Write a function sum_numbers() to get the sum of the first two integers and subtract() function that subtracts the
third integer from the result.
Wrap the two functions in a function called add_and_subtract() which will receive the three numbers

Examples:
Input:	Output:
23
6
10	    19

1
17
30	    -12

42
58
100	    0
"""


def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(result, num_3):
    return result - num_3


def add_and_subtract(num_1, num_2, num_3):
    result = sum_numbers(num_1, num_2)
    total = subtract(result, num_3)
    return total


print(add_and_subtract(int(input()), int(input()), int(input())))

