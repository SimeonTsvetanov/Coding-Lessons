distance_km = int(input())
fuel_per_100_km = int(input())
price_petrol_liter = float(input())
won_cash = int(input())

total_fuel_consumption = distance_km * fuel_per_100_km / 100
total_price_fuel = total_fuel_consumption * price_petrol_liter

if won_cash >= total_price_fuel:
    print(f"You can go home. {(won_cash - total_price_fuel):.2f} money left.")
else:
    print(f"Sorry, you cannot go home. Each will receive {(won_cash / 5):.2f} money.")
