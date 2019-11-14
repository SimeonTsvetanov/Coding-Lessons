"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#3

SUPyF2 Dict-Exercise - 04. Orders

Problem:
Write a program that keeps information about products and their prices.
Each product has a name, a price and a quantity. If the product doesn't exist yet, add it with its starting quantity.
If you receive a product, which already exists,
increase its quantity by the input quantity and if its price is different, replace the price as well.
You will receive products' names, prices and quantities on new lines.
Until you receive the command "buy", keep adding items.
When you do receive the command "buy",
print the items with their names and total price of all the products with that name.
Input
•	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
•	The product data is always delimited by a single space.
Output
•	Print information about each product in the following format:
"{productName} -> {totalPrice}"
•	Format the average grade to the 2nd digit after the decimal separator.

Examples:
Input:	            Output:
Beer 2.20 100       Beer -> 220.00
IceTea 1.50 50      IceTea -> 75.00
NukaCola 3.30 80    NukaCola -> 264.00
Water 1.00 500      Water -> 500.00
buy

Input:	            Output:
Beer 2.40 350       Beer -> 660.00
Water 1.25 200      Water -> 250.00
IceTea 5.20 100     IceTea -> 110.00
Beer 1.20 200
IceTea 0.50 120
buy

Input:	                Output:
CesarSalad 10.20 25     CesarSalad -> 255.00
SuperEnergy 0.80 400    SuperEnergy -> 320.00
Beer 1.35 350           Beer -> 472.50
IceCream 1.50 25        IceCream -> 37.50
buy
"""
products = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity

for product, value in products.items():
    print(f"{product} -> {(value[0] * value[1]):.2f}")
