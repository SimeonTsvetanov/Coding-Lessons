"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#3

SUPyF2 Functions-Exercise - 04. Odd and Even Sum

Problem:
You will receive a single number.
You have to write a function that returns the sum of all even and all odd digits from that number
 as a single string like in the examples below.

Examples:
Input:	                Output:
1000435	                Odd sum = 9, Even sum = 4
3495892137259234	    Odd sum = 54, Even sum = 22
"""


def even_and_odd_sum(number):
    odd_digits_list = [int(digit) for digit in number if digit % 2 != 0]
    even_digits_list = [int(digit) for digit in number if digit % 2 == 0]
    return f"Odd sum = {sum(odd_digits_list)}, Even sum = {sum(even_digits_list)}"


print(even_and_odd_sum([int(digit) for digit in input()]))
