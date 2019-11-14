import math

people = int(input())
budget = float(input())

count_easter_bread = math.ceil(people / 3)
count_eggs = people * 2
easter_bread = (math.ceil(people / 3)) * 4
eggs = (people * 2) * 0.45

total = easter_bread + eggs

if budget >= total:
    print(f"Lyubo bought {count_easter_bread} Easter bread and {count_eggs} eggs.")
    print(f"He has {abs(budget - total):.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(total - budget):.2f} lv. more.")
