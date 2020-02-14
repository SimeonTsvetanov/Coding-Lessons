from collections import deque

chemical_liquids = deque([int(x) for x in input().split()])
physical_items = [int(x) for x in input().split()]

base_materials = {
    25: "Glass",
    50: "Aluminium",
    75: "Lithium",
    100: "Carbon fiber"
}

collected_materials = {
    "Aluminium": 0,
    "Carbon fiber": 0,
    "Glass": 0,
    "Lithium": 0
}

while chemical_liquids and physical_items:
    liquid = chemical_liquids.popleft()
    item = physical_items.pop()
    if (liquid + item) in base_materials:
        collected_materials[base_materials[liquid + item]] += 1
    else:
        physical_items.append(item + 3)

if all(x > 0 for x in collected_materials.values()):
    print(f"Wohoo! You succeeded in building the spaceship!")
else:
    print(f"Ugh, what a pity! You didn't have enough materials to build the spaceship.")
if not chemical_liquids:
    print(f"Liquids left: none")
else:
    print(f"Liquids left: {', '.join([str(liquid) for liquid in chemical_liquids])}")
if not physical_items:
    print(f"Physical items left: none")
else:
    print(f"Physical items left: {', '.join([str(item) for item in physical_items[::-1]])}")
for advanced_item, count in collected_materials.items():
    print(f"{advanced_item}: {count}")
