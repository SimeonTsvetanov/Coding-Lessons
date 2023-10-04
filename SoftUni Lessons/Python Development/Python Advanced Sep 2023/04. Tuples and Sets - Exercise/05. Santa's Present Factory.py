from collections import deque
presents_formula = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0
}

materials = [int(num) for num in input().split()]
magic = deque([int(num) for num in input().split()])

while materials and magic:

    current_material = materials.pop()
    if current_material == 0:
        if magic[-1] == 0:
            magic.pop()
        continue
    current_magic = magic.popleft()
    if current_magic == 0:
        materials.append(current_material)
        continue
    current_present = current_magic * current_material
    if current_present in presents_formula:
        crafted_presents[presents_formula[current_present]] += 1
    elif current_present < 0:
        materials.append(current_material + current_magic)
    elif current_present > 0:
        materials.append(current_material + 15)

if (crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0) or \
        (crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for present, count in sorted(crafted_presents.items()):
    if count > 0:
        print(f"{present}: {count}")