legendary_item = None
items = {
    'shards': 0,
    'fragments': 0,
    'motes': 0,
}


def add_item(item: str, quantity: int):
    global items
    if item not in items:
        items[item] = 0
    items[item] += quantity


def check_legendary():
    global legendary_item
    quote = 250

    if items['shards'] >= quote:
        legendary_item = 'Shadowmourne'
        items['shards'] -= quote
    elif items['fragments'] >= quote:
        legendary_item = 'Valanyr'
        items['fragments'] -= quote
    elif items['motes'] >= quote:
        legendary_item = 'Dragonwrath'
        items['motes'] -= quote


while True:
    if legendary_item:
        break

    new_items = input().split(' ')

    for i in range(0, len(new_items), 2):
        item = new_items[i + 1].lower()
        quantity = int(new_items[i])

        add_item(item, quantity)
        check_legendary()

        if legendary_item:
            break

print(f"{legendary_item} obtained!")
for (item, quantity) in items.items():
    print(f"{item}: {quantity}")
