items = {}

while True:
    command = input().split(' ')
    if command[0] == "buy":
        break
    item = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if item not in items:
        items[item] = [0, 0]

    data = items[item]

    items[item][0] = price
    items[item][1] += quantity

for item, data in items.items():
    print(f"{item} -> {(data[0] * data[1]):.2f}")
