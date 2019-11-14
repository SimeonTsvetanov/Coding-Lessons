destination = input()
distance_from_earth = int(input())
budget = int(input())
fuel_consumption = float(input())
gas_price = float(input())

liters_per_gm = fuel_consumption / 100
price_per_gm = liters_per_gm * gas_price
total_price = price_per_gm * distance_from_earth

if budget >= total_price:
    print(f"Off to {destination} with ${(budget - total_price):.2f} for snacks")
else:
    print(f"Maybe another time, need ${(total_price - budget):.2f} more")
