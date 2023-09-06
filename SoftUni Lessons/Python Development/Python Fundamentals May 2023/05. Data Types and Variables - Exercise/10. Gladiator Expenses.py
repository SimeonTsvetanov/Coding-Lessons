lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = 0
sword = 0
shield = 0
armor = 0

for fight in range(1, lost_fights + 1):
    # Every second lost game, his helmet is broken
    if fight % 2 == 0:
        helmet += 1
    # Every third lost game, his sword is broken
    if fight % 3 == 0:
        sword += 1
    # When both his sword and helmet are broken in the same lost fight, his shield also breaks.
    if fight % 2 == 0 and fight % 3 == 0:
        shield += 1
        # Every second time his shield brakes, his armor also needs to be repaired.
        if shield % 2 == 0:
            armor += 1

expenses = (helmet * helmet_price) + (sword * sword_price) + (shield * shield_price) + (armor * armor_price)

print(f"Gladiator expenses: {expenses:.2f} aureus")
