bunker = {material: [] for material in input().split(", ")}
count_items = 0
total_quality = 0

for _ in range(int(input())):
    type_material, material, quantity_and_quality = input().split(" - ")
    if type_material in bunker:
        bunker[type_material].append(material)
        items_count, quality = quantity_and_quality.split(";")
        count_items += int(items_count.split(":")[1])
        total_quality += int(quality.split(":")[1])

print(f"Count of items: {count_items}")
print(f"Average quality: {(total_quality / len(bunker)):.2f}")
[print(f"{type_material} -> {', '.join(materials_list)}") for type_material, materials_list in bunker.items()]
