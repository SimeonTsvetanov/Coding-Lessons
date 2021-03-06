"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#5

SUPyF Dictionaries - 06. Exam Shopping

Problem:
A supermarket has products which have quantities. Your task is to stock the shop before Exam Sunday.
Until you receive the command “shopping time”, add the various products to the shop’s inventory,
keeping track of their quantity (for inventory purposes). When you receive the aforementioned command,
the students start pouring in before the exam and buy various products.
The format for stocking a product is: “stock {product} {quantity}”.
The format for buying a product is: “buy {product} {quantity}”.
If a student tries to buy a product, which doesn’t exist, print “{product} doesn't exist”. If it does exist,
but it’s out of stock, print “{product} out of stock”. If a student tries buying more than the quantity of that product,
 sell them all the quantity of the product (the product is left out of stock, don’t print anything).
When you receive the command “exam time”, your task is to print the remaining inventory in the following format:
“{product} -> {quantity}”. If a product is out of stock, do not print it.
Examples:
INPUT:
stock Boca_Cola 16
stock Kay's_Chips 33
stock Lobster_Energy 60
stock Boca_Cola 4
stock Loreni 15
stock Loreni 15
stock Loreni 15
stock Loreni 15
shopping time
buy Boca_Bola 2
buy Lobster_Energy 20
buy Boca_Cola 1
buy Boba_Bola 12
exam time

OUTPUT:
Boca_Bola doesn't exist
Boba_Bola doesn't exist
Boca_Cola -> 19
Kay's_Chips -> 33
Lobster_Energy -> 40
Loreni -> 60
"""

stock = {}

while True:
    command = [item for item in input().split(" ")]
    if "shopping" in command:
        break
    if command[1] not in stock:
        stock[command[1]] = int(command[2])
    elif command[1] in stock:
        stock[command[1]] += int(command[2])
while True:
    command = [item for item in input().split(" ")]
    if "exam" in command:
        break
    if command[1] not in stock:
        print(f"{command[1]} doesn't exist")
    elif command[1] in stock and stock.__getitem__(command[1]) > 0:
        stock[command[1]] -= int(command[2])
        if stock.__getitem__(command[1]) <= 0:
            stock[command[1]] = 0
    elif command[1] in stock and stock.__getitem__(command[1]) <= 0:
        print(f"{command[1]} out of stock")

for item, value in stock.items():
    if stock.__getitem__(item) > 0:
        print(f"{item} -> {value}")
