"""
Functions - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1729#0

SUPyF2 Functions-More-Exercises - 01. Data Types

Problem:
Write a program that, depending on the first line of the input, reads an int, double or string.
•	If the data type is int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.
•	If the data type is string, surround the input with "$".
Print the result on the console.

Examples:
Input	    Output
int         10
5

real        3.00
2
string      $hello$
hello

Hint:
Try to solve the problem using only one method with different overloads.
"""


def data_types():
    type_data = input()
    value = input()
    if type_data == "int":
        print(int(value) * 2)
    elif type_data == "real":
        print(f"{(float(value) * 1.5):.2f}")
    elif type_data == "string":
        print(f"${value}$")


if __name__ == '__main__':
    data_types()
