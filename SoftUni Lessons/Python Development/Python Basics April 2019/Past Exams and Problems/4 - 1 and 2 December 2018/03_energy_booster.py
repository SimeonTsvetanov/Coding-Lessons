fruit = input()
size = input()
count_sets = int(input())

price = 0

if size == "small":
    if fruit == "Watermelon":
        price = 2 * 56
    elif fruit == "Mango":
        price = 2 * 36.66
    elif fruit == "Pineapple":
        price = 2 * 42.10
    elif fruit == "Raspberry":
        price = 2 * 20
elif size == "big":
    if fruit == "Watermelon":
        price = 5 * 28.70
    elif fruit == "Mango":
        price = 5 * 19.60
    elif fruit == "Pineapple":
        price = 5 * 24.80
    elif fruit == "Raspberry":
        price = 5 * 15.20

price_sets = price * count_sets

if 400 <= price_sets <= 1000:
    price_sets -= price_sets * 0.15
elif price_sets > 1000:
    price_sets -= price_sets * 0.5

print(f"{price_sets:.2f} lv.")
