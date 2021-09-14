"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#1

02. Sign of Integer Number

Условие:
Create a function that prints the sign of an integer number n.
Examples
Input	Output
2	    The number 2 is positive.
-5	    The number -5 is negative.
0	    The number 0 is zero.
"""


def sign_of_integer(num=int(input())):
    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is zero.")


sign_of_integer()

# # Redoing the task 
# def sign_of_number(n):
#     """Create a function that prints the sign of an integer number n."""
# 
#     sign = None
# 
#     if n > 0:
#         sign = "positive"
#     elif n < 0:
#         sign = "negative"
#     else:
#         sign = "zero"
# 
#     print(f"The number {n} is {sign}.")
# 
# 
# sign_of_number(int(input()))

