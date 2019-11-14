"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#0

01. Blank Receipt

Условие:
Create a function that prints a blank cash receipt. The function should invoke three other functions:
one for printing the header, one for the body and one for the footer of the receipt.
The header should contain the following text:
CASH RECEIPT
------------------------------
The body should contain the following text:
Charged to____________________
Received by___________________
And the text for the footer:
------------------------------
© SoftUni

Examples
Output

CASH RECEIPT
------------------------------
Charged to____________________
Received by___________________
------------------------------
© SoftUni
"""


def header():
    print(f"CASH RECEIPT")
    print(f"------------------------------")


def body():
    print(f"Charged to____________________")
    print(f"Received by___________________")


def footer():
    print(f"------------------------------")
    print(f"© SoftUni")


def print_all():
    header()
    body()
    footer()


print_all()
