"""
Dictionaries - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1736#1

SUPyF2 Dictionaries-Lab - 02. Stock

Problem:
After you have successfully completed your first task, your boss decides to give you another one right away.
Now not only you have to keep track of the stock, but also you have to answer customers
if you have some products in stock or not.
You will be given key-value pairs of products and quantities (on a single line separated by space).
On the next line you will be given products to search for. Check for each product, you have 2 possibilities:
•	If you have the product, print "We have {quantity} of {product} left"
•	Otherwise, print "Sorry, we don't have {product}"

Examples:
Input:
cheese 10 bread 5 ham 10 chocolate 3
jam cheese ham tomatoes

Output:
Sorry, we don't have jam
We have 10 of cheese left
We have 10 of ham left
Sorry, we don't have tomatoes
"""

string_to_list = [item for item in input().split()]

bakery = {}

for key in range(0, len(string_to_list), 2):
    item = string_to_list[key]
    value = int(string_to_list[key + 1])
    bakery[item] = value

for request in [item for item in input().split()]:
    if request in bakery:
        print(f"We have {bakery[request]} of {request} left")
    else:
        print(f"Sorry, we don't have {request}")
