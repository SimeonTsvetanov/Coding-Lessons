change = float(input())

change *= 100
change = int(change)

count_coins = 0

while change > 0:
    if change >= 200:
        count_coins += 1
        change -= 200
    elif change >= 100:
        count_coins += 1
        change -= 100
    elif change >= 50:
        count_coins += 1
        change -= 50
    elif change >= 20:
        count_coins += 1
        change -= 20
    elif change >= 10:
        count_coins += 1
        change -= 10
    elif change >= 5:
        count_coins += 1
        change -= 5
    elif change >= 2:
        count_coins += 1
        change -= 2
    elif change >= 1:
        count_coins += 1
        change -= 1
    else:
        break

print(count_coins)
