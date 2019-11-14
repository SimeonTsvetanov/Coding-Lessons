days = int(input())
room = input()
score = input()

nights = days - 1

price = 0

if room == "room for one person":
    price = nights * 18
elif room == "apartment":
    price = nights * 25
    if nights < 10:
        price -= price * 0.3
    elif 10 <= nights <= 15:
        price -= price * 0.35
    elif nights > 15:
        price -= price * 0.5
elif room == "president apartment":
    price = nights * 35
    if nights < 10:
        price -= price * 0.1
    elif 10 <= nights <= 15:
        price -= price * 0.15
    elif nights > 15:
        price -= price * 0.2

if score == "positive":
    price += price * 0.25
elif score == "negative":
    price -= price * 0.1

print(f"{price:.2f}")

