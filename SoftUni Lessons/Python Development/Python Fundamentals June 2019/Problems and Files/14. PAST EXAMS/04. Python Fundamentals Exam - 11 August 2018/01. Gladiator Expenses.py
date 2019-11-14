import math
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = 0
broken_swords = 0
broken_shields = 0

check_for_shield = 0

for fight in range(1, lost_fights_count + 1):
    check_for_shield = 0
    if fight % 2 == 0:
        broken_helmets += 1
        check_for_shield += 1
    if fight % 3 == 0:
        broken_swords += 1
        check_for_shield += 1
    if check_for_shield == 2:
        broken_shields += 1

broken_armor = math.floor(broken_shields / 2)

total = (broken_helmets * helmet_price) + (broken_swords * sword_price) + \
        (broken_shields * shield_price) + (broken_armor * armor_price)

print(f"Gladiator expenses: {total:.2f} aureus")
