import math

group_size = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins += 50 - (group_size * 2)
    if day % 3 == 0:
        coins -= group_size * 3
    if day % 5 == 0:
        coins += 20 * group_size
        if day % 3 == 0:
            coins -= 2 * group_size

print(f"{group_size} companions received {math.floor(coins / group_size)} coins each.")