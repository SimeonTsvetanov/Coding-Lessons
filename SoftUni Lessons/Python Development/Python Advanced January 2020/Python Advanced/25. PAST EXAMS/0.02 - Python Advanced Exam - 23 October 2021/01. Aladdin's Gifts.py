def create_gift(p):
    if 100 <= p <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= p <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= p <= 399:
        gifts["Gold"] += 1
    elif 400 <= p <= 499:
        gifts["Diamond Jewellery"] += 1


materials = [int(m) for m in input().split()]
magic = [int(m) for m in input().split()]

gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}


while materials and magic:
    material, mag = materials[-1], magic[0]
    power = material + mag
    materials.remove(materials[-1]), magic.remove(magic[0])

    if 100 <= power <= 499:
        create_gift(p=power)
    elif power < 100:
        if power % 2 == 0:
            power = (material * 2) + (mag * 3)
            if 100 <= power <= 499:
                create_gift(power)
        elif power % 2 != 0:
            power = (material * 2) + (mag * 2)
            if 100 <= power <= 499:
                create_gift(power)
    elif power > 499:
        power = power / 2
        if 100 <= power <= 499:
            create_gift(power)

if ((gifts["Gemstone"] > 0) and (gifts["Porcelain Sculpture"] > 0)) \
        or ((gifts["Gold"] > 0) and (gifts["Diamond Jewellery"] > 0)):
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(m) for m in magic])}")

for gift, count in sorted(gifts.items(), key=lambda x: x[0]):
    if count > 0:
        print(f"{gift}: {count}")
