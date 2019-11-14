budget = float(input())
category = input()
people = int(input())

after_transport = 0

if 1 <= people <= 4:
    after_transport = budget - (budget * 0.75)
elif 5 <= people <= 9:
    after_transport = budget - (budget * 0.60)
elif 10 <= people <= 24:
    after_transport = budget - (budget * 0.50)
elif 25 <= people <= 49:
    after_transport = budget - (budget * 0.40)
elif people >= 50:
    after_transport = budget - (budget * 0.25)

price = 0

if category == "VIP":
    price = 499.99 * people
elif category == "Normal":
    price = 249.99 * people

if after_transport >= price:
    print(f"Yes! You have {(after_transport - price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price - after_transport):.2f} leva.")





