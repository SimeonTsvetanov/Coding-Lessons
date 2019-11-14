"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#2

SUPyF2 Dict-Exercise - 03. Legendary Farming

Problem:
You've done all the work and the last thing left to accomplish is to own a legendary item.
However, it's a tedious process and it requires quite a bit of farming.
Anyway, you are not too pretentious – any legendary item will do. The possible items are:
•	Shadowmourne – requires 250 Shards;
•	Valanyr – requires 250 Fragments;
•	Dragonwrath – requires 250 Motes;
Shards, Fragments and Motes are the key materials and everything else is junk.
You will be given lines of input, in the format:
2 motes 3 ores 15 stones
Keep track of the key materials - the first one that reaches the 250 mark, wins the race.
At that point you have to print that the corresponding legendary item is obtained.
Then, print the remaining shards, fragments, motes, ordered by quantity in descending order,
then by name in ascending order, each on a new line. Finally, print the collected junk items in alphabetical order.
Input
•	Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
Output
•	On the first line, print the obtained item in the format: {Legendary item} obtained!
•	On the next three lines, print the remaining key materials in descending order by quantity
o	If two key materials have the same quantity, print them in alphabetical order
•	On the final several lines, print the junk items in alphabetical order
o	All materials are printed in format {material}: {quantity}
o	The output should be lowercase, except for the first letter of the legendary

Examples:
Input:
3 Motes 5 stones 5 Shards
6 leathers 255 fragments 7 Shards

Output:
Valanyr obtained!
fragments: 5
shards: 5
motes: 3
leathers: 6
stones: 5

Input:
123 silver 6 shards 8 shards 5 motes
9 fangs 75 motes 103 MOTES 8 Shards
86 Motes 7 stones 19 silver

Output:
Dragonwrath obtained!
shards: 22
motes: 19
fragments: 0
fangs: 9
silver: 123
"""

materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}
junk = {}

legendary_item = None

while True:
    if legendary_item:
        break
    data = [item for item in input().split()]
    for i in range(0, len(data), 2):
        material = data[i + 1].lower()
        quantity = int(data[i])
        if material != "shards" and material != "fragments" and material != "motes":
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

        else:
            materials[material] += quantity

            if materials["shards"] >= 250:
                legendary_item = "Shadowmourne"
                materials["shards"] -= 250
                break
            if materials["fragments"] >= 250:
                legendary_item = "Valanyr"
                materials["fragments"] -= 250
                break
            if materials["motes"] >= 250:
                legendary_item = "Dragonwrath"
                materials["motes"] -= 250
                break

print(f"{legendary_item} obtained!")

for item, value in sorted(materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{item}: {value}")
for item, value in sorted(junk.items(), key=lambda x: x):
    print(f"{item}: {value}")
