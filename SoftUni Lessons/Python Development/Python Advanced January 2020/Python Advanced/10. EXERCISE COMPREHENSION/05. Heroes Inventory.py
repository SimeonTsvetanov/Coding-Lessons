heroes = {hero: {} for hero in input().split(", ")}

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    name = command[0]
    item = command[1]
    cost = int(command[2])
    if name in heroes:
        if item not in heroes[name]:
            heroes[name][item] = cost

for hero, items in heroes.items():
    print(f"{hero} -> Items: {len(items)}, Cost: {sum([amount for item, amount in items.items()])}")
