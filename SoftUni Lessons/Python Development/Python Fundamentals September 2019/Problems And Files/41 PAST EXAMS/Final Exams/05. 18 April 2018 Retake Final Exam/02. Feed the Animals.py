"""
Technology Fundamentals Retake Final Exam - 18 April 2018
link: https://judge.softuni.bg/Contests/Practice/Index/1612#1
Name: 02. Feed the Animals
"""

all_animals = {}
areas = {}

while True:
    command = input().split(":")
    if command[0] == "Last Info":
        break
    elif command[0] == "Add":
        animal_name = command[1]
        daily_food_limit = int(command[2])
        area = command[3]
        if animal_name not in all_animals:
            all_animals[animal_name] = [daily_food_limit, area]
        elif animal_name in all_animals:
            all_animals[animal_name][0] += daily_food_limit

    elif command[0] == "Feed":
        feed_animal_name = command[1]
        feed_food = int(command[2])
        feed_area = command[3]
        if feed_animal_name in all_animals:
            all_animals[feed_animal_name][0] -= feed_food
            if all_animals[feed_animal_name][0] <= 0:
                print(f"{feed_animal_name} was successfully fed")
                del all_animals[feed_animal_name]

for animal, values in all_animals.items():
    if values[1] not in areas:
        areas[values[1]] = 1
    elif values[1] in areas:
        areas[values[1]] += 1

print(f"Animals:")
for animal, values in sorted(all_animals.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{animal} -> {values[0]}g")

print(f"Areas with hungry animals:")
for area, count in sorted(areas.items(), key=lambda x: -x[1]):
    print(f"{area} : {count}")

