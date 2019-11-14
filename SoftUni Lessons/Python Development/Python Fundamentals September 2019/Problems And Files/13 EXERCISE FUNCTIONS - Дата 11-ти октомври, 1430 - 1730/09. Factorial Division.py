"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#8

SUPyF2 Functions-Exercise - 09. Factorial Division (not included in final score)

Problem:
Write a function that receives two integer numbers.
Calculate factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.
Examples
Input	Output		Input	Output
5       60.00       6       360.00
2	    		    2


Hints
•	Read more about factorial here: https://en.wikipedia.org/wiki/Factorial

"""


def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


def factorial_division(num_1, num_2):
    return print(f"{(get_factorial(num_1) / get_factorial(num_2)):.2f}")


factorial_division(int(input()), int(input()))
