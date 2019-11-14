"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#6

SUPyF2 Lists-Advanced-Exercise - 08. Feed the Animals (not included in final score)

Problem:
The sanctuary needs to provide food for the animals and feed them, so your task is to help with the process
Create a program that organizes the daily feeding of animals. You need to keep information about animals,
their daily food limit and the areas of the Wildlife Refuge they live in.
You will be receiving lines with commands until you receive the "Last Info" message.  There are two possible commands:
•	"Add:{animalName}:{dailyFoodLimit}:{area}":
o	Add the animal and its daily food limit to your records.
    It is guaranteed that the names of the animals are unique and there will never be animals with the same name.
    If it already exists, just increase the value of the daily food limit with the current one that is given.
•	"Feed:{animalName}:{food}:{area}":
o	Check if the animal exists and if it does, reduce its daily food limit with the given food for feeding.
    If its limit reaches 0 or less, the animal is considered successfully fed and you need to remove it from
    your records and print the following message:
	"{animalName} was successfully fed"
You need to know the count of hungry animals there are left in each area in the end.
If an animal has daily food limit above 0, it is considered hungry.
In the end, you have to print each animal with its daily food limit sorted in descending order by the daily food limit
and then by its name in ascending order in the following format:
Animals:
{animalName} -> {dailyFoodLimit}g
{animalName} -> {dailyFoodLimit}g
Afterwards, print the areas with the count of animals, which are not fed in descending order by the count of animals.
If an area has 0 hungry animals in it, don't print it. The output must be in the following format:
Areas with hungry animals:
{areaName} : {countOfUnfedAnimals}
{areaName} : {countOfUnfedAnimals}
Input / Consrtaints
•	You will be receiving lines until you receive the "Last Info" command.
•	The food comes in grams and is an integer number in the range [1...100000].
•	The input will always be valid.
•	There will never be a case, in which an animal is in two or more areas at the same time.
Output
•	Print the appropriate message after the "Feed" command, if an animal is fed.
•	Print the animals with their daily food limit in the format described above.
•	Print the areas with the count of unfed animals in them in the format described above.

Examples:
Input:
Add:Maya:7600:WaterfallArea
Add:Bobbie:6570:DeepWoodsArea
Add:Adam:4500:ByTheCreek
Add:Jamie:1290:RiverArea
Add:Gem:8730:WaterfallArea
Add:Maya:1230:WaterfallArea
Add:Jamie:560:RiverArea
Feed:Bobbie:6300:DeepWoodsArea
Feed:Adam:4650:ByTheCreek
Feed:Jamie:2000:RiverArea
Last Info

Output:
Adam was successfully fed
Jamie was successfully fed
Animals:
Maya -> 8830g
Gem -> 8730g
Bobbie -> 270g
Areas with hungry animals:
WaterfallArea : 2
DeepWoodsArea : 1

Comments:
First, we receive the "Add" command, so we add "Maya" to our records and we keep her daily food limit - 7600.
We know that she is in WaterfallArea. We keep adding the new animals until we receive "Maya" again and we have
to increase her food limit with 1230, so it becomes 8830.
After that we receive "Jamie" and we need to increase his daily food limit with 560, after which it becomes 1850.
Then we start receiving "Feed" commands. First, we must decrease Bobbie's food limit with 6300,
so it becomes 270. Then, we need to decrease Adam's food limit with 4650.
It becomes less than zero and we remove him from the collection – he is considered fed,
respectively that is one less hungry animal in the area that he is in – ByTheCreek.
Then we "Feed" Jamie with 2000 and his limit becomes less than zero, so we print "Jamie was successfully fed"
and we remove him from our records and note that there is one less hungry animal in his area – RiverArea. In the end,
we print the animals we still have in our collection,
with their daily food limits in descending order by the food limits.
Afterwards we print only the areas in which there are remaining hungry animals and their count in descending order.
"""


class Animal:
    def __init__(self, name: str, food: int, area: str):
        self.name = name
        self.food = food
        self.area = area


class Area:
    def __init__(self, name: str, animals: list):
        self.name = name
        self.animals = animals


zoo = []

while True:
    data = input()
    if data == "Last Info":
        break
    add_or_feed, a_name, a_food, a_area = data.split(":")
    if add_or_feed == "Add":
        area_in_zoo = False
        for area in zoo:
            if area.name == a_area:
                area_in_zoo = True
                animal_in_area = False
                for animal in area.animals:
                    if animal.name == a_name:
                        animal_in_area = True
                        animal.food += int(a_food)
                        break
                if not animal_in_area:
                    new_animal_for_area = Animal(name=a_name, food=int(a_food), area=a_area)
                    area.animals += [new_animal_for_area]
        if not area_in_zoo:
            new_animal = Animal(name=a_name, food=int(a_food), area=a_area)
            new_area = Area(name=a_area, animals=[new_animal])
            zoo += [new_area]
    elif add_or_feed == "Feed":
        for area in zoo:
            if area.name == a_area:
                for animal in area.animals:
                    if animal.name == a_name:
                        animal.food -= int(a_food)
                        if animal.food <= 0:
                            area.animals.remove(animal)
                            print(f"{a_name} was successfully fed")

only_animals = []
for area in zoo:
    for animal in area.animals:
        only_animals += [animal]

only_animals = sorted(sorted(only_animals, key=lambda x: x.name), key=lambda x: x.food, reverse=True)
print("Animals:")
for animal in only_animals:
    print(f"{animal.name} -> {animal.food}g")
print("Areas with hungry animals:")
zoo = sorted(zoo, key=lambda x: len(x.animals), reverse=True)
for area in zoo:
    if len(area.animals) > 0:
        print(f"{area.name} : {len(area.animals)}")



