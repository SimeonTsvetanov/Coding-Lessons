pastry = input()
count_pastry = int(input())
day = int(input())

price = 0

if day <= 15:
    if pastry == "Cake":
        price = 24 * count_pastry
    elif pastry == "Souffle":
        price = 6.66 * count_pastry
    elif pastry == "Baklava":
        price = 12.60 * count_pastry
elif day > 15:
    if pastry == "Cake":
        price = 28.70 * count_pastry
    elif pastry == "Souffle":
        price = 9.80 * count_pastry
    elif pastry == "Baklava":
        price = 16.98 * count_pastry

if 100 <= price <= 200:
    price -= price * 0.15
elif price > 200:
    price -= price * 0.25

if day <= 15:
    price -= price * 0.1

print(f"{price:.2f}")
