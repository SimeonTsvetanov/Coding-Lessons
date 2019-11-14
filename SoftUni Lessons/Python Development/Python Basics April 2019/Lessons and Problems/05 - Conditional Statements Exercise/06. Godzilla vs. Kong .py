budget = float(input())
people = int(input())
price_dress = float(input())

decoration = budget * 0.1
total_dress = people * price_dress

if people > 150:
    total_dress = total_dress - (total_dress * 0.1)

expenses = decoration + total_dress

if expenses > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(expenses - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - expenses):.2f} leva left.")



