budget = int(input())
count = int(input())

for i in range(count):
    stock = input()
    if stock == "hoodie":
        budget -= 30
    elif stock == "keychain":
        budget -= 4
    elif stock == "T-shirt":
        budget -= 20
    elif stock == "flag":
        budget -= 15
    elif stock == "sticker":
        budget -= 1

if budget < 0:
    print(f"Not enough money, you need {abs(budget)} more lv.")

if budget >= 0:
    print(f"You bought {count} items and left with {budget} lv.")
