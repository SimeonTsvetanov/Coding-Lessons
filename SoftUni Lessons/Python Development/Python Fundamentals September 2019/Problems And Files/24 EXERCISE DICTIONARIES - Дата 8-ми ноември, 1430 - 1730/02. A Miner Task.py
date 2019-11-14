"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#1

SUPyF2 Dict-Exercise - 02. A Miner Task

Problem:
You will be given a sequence of strings, each on a new line. Every odd line on the console
is representing a resource (e.g. Gold, Silver, Copper, and so on) and every even – quantity.
Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
{resource} –> {quantity}
The quantities will be in the range [1 … 2 000 000 000]
Examples
Input
Gold
155
Silver
10
Copper
17
stop

Output:
Gold -> 155
Silver -> 10
Copper -> 17

Input:
gold
155
silver
10
copper
17
gold
15
stop

Output:
gold -> 170
silver -> 10
copper -> 17
"""
resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
