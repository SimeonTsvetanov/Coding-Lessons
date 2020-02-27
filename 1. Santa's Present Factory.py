from collections import deque

materials = list(map(int, input().split()))
magic_values = deque(list(map(int, input().split())))

presents = {
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

while materials and magic_values:
    current_material = materials.pop()
    current_magic = magic_values.popleft()
    total_magic = current_material * current_magic

    if total_magic in presents:
        crafted_presents[presents[total_magic]] += 1
    else:
        if total_magic > 0:
            materials.append(current_material + 15)
        elif total_magic < 0:
            result = current_material + current_magic
            materials.append(result)
        else:
            if current_material:
                materials.append(current_material)
            if current_magic:
                magic_values.appendleft(current_magic)

success = (crafted_presents["Doll"] and crafted_presents["Wooden train"]) or \
          (crafted_presents["Teddy bear"] and crafted_presents["Bicycle"])

if success:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for item, value in sorted(crafted_presents.items()):
    if value > 0:
        print(f"{item}: {value}")
