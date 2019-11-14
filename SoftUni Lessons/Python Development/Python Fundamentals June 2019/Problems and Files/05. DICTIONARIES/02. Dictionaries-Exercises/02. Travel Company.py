"""
Dictionaries - Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1088#1

SUPyF Dictionaries Exercises - 02. Travel Company

Problem:
Write a program, which categorizes information about a travel company.
Companies have various vehicles planned for different cities. Every city has prepared several types of vehicles.
Each vehicle type has a different capacity.
Until you receive the command “ready”, you will receive all the cities the company offers holiday packages for,
and their respective vehicle types + capacities in the format:
- “{city}:{type}-{capacity},{type}-{capacity}…”
An example city with its transportation options would look like this:
- “Athens:bus-40,airplane-300,train-150”
If a city is entered a second time, add all transport which hasn’t already been added and replace existing transports’
capacities with the new ones.
After the “ready” command, you will start receiving groups for various cities in the format: “{city} {peopleCount}”
until you receive “travel time!”.
After that, calculate whether the group will have enough seats to accommodate the passengers and print the status per
these conditions:
If the group’s size is smaller than or equal to the combines seats in all the vehicles, print:
- “{city} -> all {peopleCount} accommodated”
If the group’s size is larger than the combines seats in all the vehicles, print:
- “{city} -> all except {peopleCount - transportCapacities} accommodated”
Constraints
- There will be no redundant whitespaces anywhere in the input.
- The input will always be in the format specified.
- The group cities will always be existing cities.
- The group sizes will always be positive.
EXAMPLES:
    INPUT <<<
Athens:bus-40,airplane-300,train-150
Athens:minibus-8,airplane-350
Warsaw:bus-30,train-150,airplane-120
ready
Athens 400
Warsaw 500
travel time!
    OUTPUT:
Athens -> all 400 accommodated
Warsaw -> all except 200 accommodated
"""

cities = {}

while True:
    command = input()
    if command == "ready":
        break
    a = [item for item in command.split(":")]
    city = a[0]

    b = [item for item in a[1].split(",")]

    for i in b:
        c = [item for item in i.split("-")]
        if city not in cities:
            cities[city] = {}
        cities[city][c[0]] = int(c[1])
for city, transport in cities.items():
    cities[city] = sum(transport.values())

while True:
    command = input()
    if command == "travel time!":
        break
    a = [item for item in command.split(" ")]
    check_city = a[0]
    value = int(a[1])
    if check_city in cities:
        if value <= cities[check_city]:
            print(f"{check_city} -> all {value} accommodated")
        else:
            print(f"{check_city} -> all except {abs(cities[check_city] - value)} accommodated")














