import math

name = input()
budget = float(input())
count_beer = int(input())
count_chips = int(input())

price_beers = 1.2 * count_beer
price_chips = math.ceil((price_beers * 0.45) * count_chips)

total_price = price_beers + price_chips

if budget >= total_price:
    print(f"{name} bought a snack and has {(budget - total_price):.2f} leva left.")
else:
    print(f"{name} needs {(total_price - budget):.2f} more leva!")

