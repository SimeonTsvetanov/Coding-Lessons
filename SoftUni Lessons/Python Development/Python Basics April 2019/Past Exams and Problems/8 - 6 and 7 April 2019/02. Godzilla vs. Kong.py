budget = float(input())
people_count = int(input())
one_dress = float(input())

decor = budget * 0.1
dresses = people_count * one_dress

if people_count > 150:
    dresses -= dresses * 0.1

total = dresses + decor

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(total - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(budget - total):.2f} leva left.")

