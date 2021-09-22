"""
Objects and Classes - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1733#3

SUPyF2 Objects/Classes-Lab - 04. Zoo

Problem:
Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals
in the zoo. The __init__ method should only receive the name of the zoo.
There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
•	add_animal(species, name) - based on the species adds the name to the corresponding list
•	get_info(species) - based on the species returns a string in the following format:
    "{Species} in {zoo_name}: {names}" and on another line "Total animals: {total_animals}"
On the first line you will receive the name of the zoo. On the second line you will receive number n.
On the next n lines you will receive animal info in the format: "{species} {name}".
Add the animal to the zoo to the corresponding list. The "species" command will be mammal, fish or birds.
On the final line you will receive a spices. At the end,
print all the info for that species and the total count of animals.

Example:
Input:
Great Zoo
5
mammal lion
mammal bear
fish salmon
birds owl
mammal tiger
mammal

Output:
Mammals in Great Zoo: lion, bear, tiger
Total animals: 5
"""


class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes: {', '.join(self.fishes)}\n"
        elif species == "birds":
            result += f"Birds: {', '.join(self.birds)}\n"
        result += f"Total animals: {zoo.__animals}"
        return result


zoo_name, count_animals = input(), int(input())
zoo = Zoo(name=zoo_name)
for animal in range(count_animals):
    spice, animal_kind = input().split()
    zoo.add_animal(species=spice, name=animal_kind)
print(zoo.get_info(input()))


def zoo_advanced_solution():
    class Zoo:
        __animals = 0

        def __init__(self, name: str):
            self.name = name
            self.mammal = []
            self.fish = []
            self.bird = []

        def add_animal(self, species, name):
            getattr(self, species).append(name)
            Zoo.__animals += 1

        def get_info(self, species):
            animals = "Mammals" if species == "mammal" else "Fishes" if species == "fish" else "Birds"
            return f"{animals} in {self.name}: {', '.join(getattr(self, species))}\nTotal animals: {Zoo.__animals}"

    zoo = Zoo(name=input())

    for i in range(int(input())):
        animal = input().split(" ")
        zoo.add_animal(species=animal[0], name=animal[1])

    print(zoo.get_info(input()))


zoo_advanced_solution()
