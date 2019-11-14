"""
Functions - More Exercises
Check your code: 05. Multiplication Sign

SUPyF2 Functions-More-Exercises - 05. Multiplication Sign

Problem:
You are given a number num1, num2 and num3. Write a program that finds if num1 * num2 * num3 (the product) is negative,
positive or zero. Try to do this WITHOUT multiplying the 3 numbers.
Examples
Input	Output		Input	Output
2       negative    2       positive
3                   3
-1	                1
"""


def multiplication_sign():
    a, b, c = float(input()), float(input()), float(input())
    if a > 0 and b > 0 and c > 0:
        print("positive")
    elif a == 0 or b == 0 or c == 0:
        print("zero")
    else:
        print("negative")


if __name__ == '__main__':
    multiplication_sign()
