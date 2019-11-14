budget = int(input())
season = input()
people = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if people <= 6:
    price -= price * 0.1
elif 7 <= people <= 11:
    price -= price * 0.15
elif people >= 12:
    price -= price * 0.25

if season == "Spring" or season == "Summer" or season == "Winter":
    if people % 2 == 0:
        price -= price * 0.05

if budget >= price:
    print(f"Yes! You have {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price - budget):.2f} leva.")
