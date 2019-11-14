"""
Dictionaries - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1736#2

SUPyF2 Dictionaries-Lab - 03 Statistics

Problem:
You seem to be doing great at your first job.
You have now successfully completed the first 2 of your tasks and your boss decides to give you as your
next task something more challenging. You have to accept all the new products coming in the bakery and
finally gather some statistics.
You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
Sometimes you may receive a product more than once. In that case you have to add the new quantity to the existing one.
When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"
Example:
Input:
bread: 4
cheese: 2
ham: 1
bread: 1
statistics

Output:
Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8
"""
stock = {}

while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    product = command[0]
    value = int(command[1])
    if product not in stock:
        stock[product] = value
    else:
        stock[product] += value

print("Products in stock:")
for item, value in stock.items():
    print(f"- {item}: {value}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
