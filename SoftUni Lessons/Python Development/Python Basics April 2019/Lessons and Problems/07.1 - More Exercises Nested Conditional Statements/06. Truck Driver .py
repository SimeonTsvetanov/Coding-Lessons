season = input()
km_month = float(input())

price = 0

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = (km_month * 0.75) * 4
    elif season == "Summer":
        price = (km_month * 0.9) * 4
    elif season == "Winter":
        price = (km_month * 1.05) * 4
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = (km_month * 0.95) * 4
    elif season == "Summer":
        price = (km_month * 1.1) * 4
    elif season == "Winter":
        price = (km_month * 1.25) * 4
elif 10000 < km_month <= 20000:
    price = (km_month * 1.45) * 4

price -= price * 0.1
print(f"{price:.2f}")

