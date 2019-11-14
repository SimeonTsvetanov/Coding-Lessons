people = int(input())
price_one = float(input())
budget = float(input())

cake = budget * 0.1
price = people * price_one

if 10 <= people <= 15:
    price -= price * 0.15
elif 15 < people <= 20:
    price -= price * 0.20
elif people > 20:
    price -= price * 0.25

total = price + cake

if budget >= total:
    print(f"It is party time! {abs(budget - total):.2f} leva left.")
else:
    print(f"No party! {abs(total - budget):.2f} leva needed.")
