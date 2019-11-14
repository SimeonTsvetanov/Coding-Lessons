budget = float(input())
fuel = float(input())
day = input()

fuel_price = fuel * 2.1

total = fuel_price + 100

if day == "Saturday":
    total -= total * 0.1
elif day == "Sunday":
    total -= total * 0.2

if budget >= total:
    print(f"Safari time! Money left: {abs(budget - total):.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {abs(total - budget):.2f} lv.")

