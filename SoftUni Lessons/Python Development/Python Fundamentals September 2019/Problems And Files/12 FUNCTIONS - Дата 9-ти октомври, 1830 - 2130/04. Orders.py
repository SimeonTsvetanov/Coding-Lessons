"""
Functions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1727#3

SUPyF2 Functions-Lab - 04. Orders

Problem:
Write a function that calculates the total price of an order and prints it on the console.
The function should receive one of the following products: coffee, coke, water, snacks; and a quantity of the product.
The prices for a single piece of each product are:
•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00
Print the result formatted to the second decimal place.

Example:
Input:	    Output:

water
5	        5.00

coffee
2	        3.00
"""


def order():
    product = input()
    quantity = int(input())
    if product == "coffee":
        product = 1.50
    elif product == "coke":
        product = 1.40
    elif product == "water":
        product = 1.00
    elif product == "snacks":
        product = 2.00
    print(f"{(product * quantity):.2f}")


if __name__ == '__main__':
    order()
