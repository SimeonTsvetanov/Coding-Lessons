"""
Functions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1727#1

SUPyF2 Functions-Lab - 02. Calculations

Problem:
Create a function that receives three parameters and calculates a result depending on operator.
The operator can be  'multiply', 'divide', 'add', 'subtract' .
The input comes as three parameters – two integers and an operator as a string.

Example:
Input:	    Output:
subtract
5
4	        1

divide
8
4	        2
"""


def calculator(operator, first_number, second_number):
    if operator == "multiply":
        operator = "*"
    elif operator == "divide":
        operator = "/"
    elif operator == "add":
        operator = "+"
    elif operator == "subtract":
        operator = "-"
    return eval(f"{first_number}{operator}{second_number}")


print(int(calculator(input(), input(), input())))
