"""
Dictionaries - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1738#4

SUPyF2 Dict-More-Ex. - 05. Dragon Army

Problem:
Heroes III is the best game ever. Everyone loves it and everyone plays it all the time.
Stamat is no exclusion to this rule. His favorite units in the game are all types of dragons –
black, red, gold, azure etc… He likes them so much that he gives them names and keeps logs of their stats:
damage, health and armor. The process of aggregating all the data is quite tedious,
so he would like to have a program doing it. Since he is no programmer, it's your task to help him.
You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats.
Type is preserved as in the order of input, but dragons are sorted alphabetically by name.
For each type, you should also print the average damage, health and armor of the dragons.
For each dragon, print his own stats.
There may be missing stats in the input, though. If a stat is missing you should assign it default values.
Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by null.
The input is in the following format {type} {name} {damage} {health} {armor}.
Any of the integers may be assigned null value. See the examples below for better understanding of your task.
If the same dragon is added a second time, the new stats should overwrite the previous ones.
Two dragons are considered equal if they match by both name and type.
Input
•	On the first line, you are given number N -> the number of dragons to follow
•	On the next N lines, you are given input in the above described format.
There will be single space separating each element.
Output
•	Print the aggregated data on the console
•	For each type, print average stats of its dragons in format {Type}::({damage}/{health}/{armor})
•	Damage, health and armor should be rounded to two digits after the decimal separator
•	For each dragon, print its stats in format -{Name} -> damage: {damage}, health: {health}, armor: {armor}
Constraints
•	N is in range [1…100]
•	The dragon type and name are one word only, starting with capital letter.
•	Damage health and armor are integers in range [0 … 100000] or null

Examples:
Input:
5
Red Bazgargal 100 2500 25
Black Dargonax 200 3500 18
Red Obsidion 220 2200 35
Blue Kerizsa 60 2100 20
Blue Algordox 65 1800 50

Output:
Red::(160.00/2350.00/30.00)
-Bazgargal -> damage: 100, health: 2500, armor: 25
-Obsidion -> damage: 220, health: 2200, armor: 35
Black::(200.00/3500.00/18.00)
-Dargonax -> damage: 200, health: 3500, armor: 18
Blue::(62.50/1950.00/35.00)
-Algordox -> damage: 65, health: 1800, armor: 50
-Kerizsa -> damage: 60, health: 2100, armor: 20

Input:
4
Gold Zzazx null 1000 10
Gold Traxx 500 null 0
Gold Xaarxx 250 1000 null
Gold Ardrax 100 1055 50

Output:
Gold::(223.75/826.25/17.50)
-Ardrax -> damage: 100, health: 1055, armor: 50
-Traxx -> damage: 500, health: 250, armor: 0
-Xaarxx -> damage: 250, health: 1000, armor: 10
-Zzazx -> damage: 45, health: 1000, armor: 10
"""

# -------------------------------------------------------------------------------------------------------
# There are two ways to sort This problem one of them will be to use Objects/Classes and that is it:
# -------------------------------------------------------------------------------------------------------

"""
all_dragons = []
type_dragons = []


class Dragon:
    def __init__(self, type_dragon: str, name: str, damage, health, armor):
        self.type_dragon = type_dragon
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor
        self.add_dragon()

    def add_dragon(self):
        global all_dragons
        global type_dragons
        dragon_in_all_dragons = False
        for dragon in all_dragons:
            if dragon.name == self.name:
                if dragon.type_dragon == self.type_dragon:
                    dragon_in_all_dragons = True
                    dragon.damage = self.damage
                    dragon.health = self.health
                    dragon.armor = self.armor
        if not dragon_in_all_dragons:
            all_dragons += [self]
        if self.type_dragon not in type_dragons:
            type_dragons += [self.type_dragon]

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if value != "null":
            self.__damage = int(value)
        else:
            self.__damage = 45

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value != "null":
            self.__health = int(value)
        else:
            self.__health = 250

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        if value != "null":
            self.__armor = int(value)
        else:
            self.__armor = 10


for each_time in range(int(input())):
    data = input().split()
    dg = Dragon(data[0], data[1], data[2], data[3], data[4])

for type_dr in type_dragons:
    current_types = []
    current_total_damage = 0
    current_total_health = 0
    current_total_armor = 0
    for dr in all_dragons:
        if dr.type_dragon == type_dr:
            current_types += [dr]
            current_total_damage += dr.damage
            current_total_health += dr.health
            current_total_armor += dr.armor
    average_damage = current_total_damage / len(current_types)
    average_health = current_total_health / len(current_types)
    average_armor = current_total_armor / len(current_types)
    print(f"{type_dr}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for d in sorted(current_types, key=lambda x: x.name):
        print(f"-{d.name} -> damage: {d.damage}, health: {d.health}, armor: {d.armor}")
"""

# -------------------------------------------------------------------------------------------------------
# The Second way will be to use Dictionaries and that is it:
# -------------------------------------------------------------------------------------------------------

all_dragons = {}

for how_many_times in range(int(input())):
    n_d_t, n_d_n, n_d_d, n_d_h, n_d_a = input().split()

    if n_d_d == "null":
        n_d_d = 45
    if n_d_h == "null":
        n_d_h = 250
    if n_d_a == "null":
        n_d_a = 10

    if n_d_t not in all_dragons:
        all_dragons[n_d_t] = {
            n_d_n: [int(n_d_d), int(n_d_h), int(n_d_a)]}
    else:
        all_dragons[n_d_t].update({
            n_d_n: [int(n_d_d), int(n_d_h), int(n_d_a)]})

for dragon_type, all_dragons in all_dragons.items():
    total_damage, total_health, total_armor = 0, 0, 0
    for dragon_name, dragon_data in all_dragons.items():
        total_damage += dragon_data[0]
        total_health += dragon_data[1]
        total_armor += dragon_data[2]
    all_dr = len(all_dragons)
    print(f"{dragon_type}::({(total_damage / all_dr):.2f}/{(total_health / all_dr):.2f}/{(total_armor / all_dr):.2f})")
    for dragon_name, data in sorted(all_dragons.items(), key=lambda x: x):
        print(f"-{dragon_name} -> damage: {data[0]}, health: {data[1]}, armor: {data[2]}")
