import math

star_name = input()
star_distance = int(input())
budget = int(input())
mileage = float(input())
gas_price = float(input())

liters_per_gm = mileage / 100

price_per_gigameter = liters_per_gm * gas_price

total = price_per_gigameter * star_distance

if total <= budget:
	print(f'Off to {star_name} with ${budget - total:.2f} for snacks')
else:
	print(f'Maybe another time, need ${total - budget:.2f} more')
