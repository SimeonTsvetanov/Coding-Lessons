"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#3

04. Draw a Filled Square

Условие:
Draw at the console a filled square of size n like in the example:
Examples
Input:
4
Output:
--------
-\/\/\/-
-\/\/\/-
--------

Hints
1.	Read the input
2.	Create a function which will print the top and the bottom rows (they are the same).
Don’t forget to give it a descriptive name and to give it as a parameter some length
3.	Create the function which will print the middle rows.
4.	Use the functions that you've just created to draw a square.
"""


num = int(input())


def top_and_bottom():
    for i in range(num * 2):
        print(f"-", end="")
    print()


def filling():
    print(f"-", end="")
    for i in range(int(((num * 2) - 2) / 2)):
        print(f"\/", end="")
    print(f"-", end="")
    print()


def square():
    top_and_bottom()
    for i in range(num - 2):
        filling()
    top_and_bottom()


square()

