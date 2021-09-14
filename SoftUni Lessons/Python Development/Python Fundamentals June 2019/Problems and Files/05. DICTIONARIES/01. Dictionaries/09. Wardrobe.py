"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#8

SUPyF Dictionaries - 09. Wardrobe

Problem:
You just bought a new wardrobe. The weird thing about it is that it came prepackaged with a big box of clothes
(just like those refrigerators, which ship with free beer inside them)! So, you’ll need to find something to wear.
Input
On the first line of the input, you will receive n –  the number of lines of clothes,
which came prepackaged for the wardrobe.
On the next n lines, you will receive the clothes for each color in the format:
- “{color} -> {item1},{item2},{item3}…”
If a color is added a second time, add all items from it and count the duplicates.
Finally, you will receive the color and item of the clothing, that you need to look for.
Output
Go through all the colors of the clothes and print them in the following format:
{color} clothes:
* {item1} - {count}
* {item2} - {count}
* {item3} - {count}
…
* {itemN} - {count}
If the color lines up with the clothing item, print “(found!)” alongside the item. See the examples to better
understand the output.
Example:
INPUT:
4
Blue -> dress,jeans,hat
Gold -> dress,t-shirt,boxers
White -> briefs,tanktop
Blue -> gloves
Blue dress
OUTPUT:
Blue clothes:
* dress - 1 (found!)
* jeans - 1
* hat - 1
* gloves - 1
Gold clothes:
* dress - 1
* t-shirt - 1
* boxers - 1
White clothes:
* briefs - 1
* tanktop - 1
"""
colors = {}

for each_time in range((int(input()))):
    command = [item for item in input().split(" -> ")]
    values = [item for item in command[1].split(",")]

    for value in values:
        if command[0] not in colors:
            colors[command[0]] = {}
            colors[command[0]][value] = 1
        elif command[0] in colors:
            if value not in colors[command[0]]:
                colors[command[0]][value] = 1
            elif value in colors[command[0]]:
                colors[command[0]][value] += 1

command_check = [item for item in input().split(" ")]

for color, item in colors.items():
    print(f"{color} clothes:")
    for values, count in item.items():
        if command_check[0] == color and command_check[1] == values:
            print(f"* {values} - {count} (found!)")
        else:
            print(f"* {values} - {count}")
            
            
            
 def another_solution():
    wardrobe = {}

    for each_time in range(int(input())):
        command = input().split(" -> ")
        color = command[0]
        new_clothes = command[1].split(",")
        if color not in wardrobe.keys():
            wardrobe[color] = {}
            for cloth in new_clothes:
                if cloth not in wardrobe[color].keys():
                    wardrobe[color][cloth] = new_clothes.count(cloth)
        else:
            for cloth in new_clothes:
                if cloth not in wardrobe[color].keys():
                    wardrobe[color][cloth] = 1
                else:
                    wardrobe[color][cloth] += 1

    command_check = [item for item in input().split(" ")]

    for color, item in wardrobe.items():
        print(f"{color} clothes:")
        for values, count in item.items():
            if command_check[0] == color and command_check[1] == values:
                print(f"* {values} - {count} (found!)")
            else:
                print(f"* {values} - {count}")


# another_solution()
