flower_type = input()
count = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price = 5 * count
    if count > 80:
        price -= price * 0.1
elif flower_type == "Dahlias":
    price = 3.8 * count
    if count > 90:
        price -= price * 0.15
elif flower_type == "Tulips":
    price = 2.8 * count
    if count > 80:
        price -= price * 0.15
elif flower_type == "Narcissus":
    price = 3 * count
    if count < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = 2.5 * count
    if count < 80:
        price += price * 0.2

if budget >= price:
    print(f"Hey, you have a great garden with {count} {flower_type} and {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(price - budget):.2f} leva more.")
