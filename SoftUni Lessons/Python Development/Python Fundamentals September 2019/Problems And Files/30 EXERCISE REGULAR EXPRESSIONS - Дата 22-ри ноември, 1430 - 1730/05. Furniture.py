"""
Regular Expressions - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1743#4

Name: 05. Furniture

Problem:
Write a program to calculate the total cost of different types of furniture.
You will be given some lines of input until you receive the line "Purchase".
For the line to be valid it should be in the following format:
">>{furniture name}<<{price}!{quantity}"
The price can be floating point number or whole number. Store the names of the furniture and the total price.
At the end print the each bought furniture on separate line in the format:
"Bought furniture:
{1st name}
{2nd name}
…"
And on the last line print the following: "Total money spend: {spend money}" formatted to the second decimal point.

Examples:
Input:
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase
Output:
Bought furniture:
Sofa
TV
Total money spend: 2436.69
Comments:
Only the Sofa and the TV are valid, for each of them we multiply the price by the quantity and print the result
"""
import re

pattern = r"^>>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)$"
furniture = []
total_money = 0
while True:
    line = input()
    if line == "Purchase":
        break
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))
        furniture.append(name)
        total_money += price * quantity

print(f"Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_money:.2f}")
