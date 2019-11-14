days = int(input()) - 1
room_type = input()
score = input()

price = 0

if room_type == "apartment":
    price = 25.00 * days
    if days < 10:
        price = price - (price * 0.3)
    elif 10 <= days <= 15:
        price = price - (price * 0.35)
    elif days > 15:
        price = price - (price * 0.5)
elif room_type == "president apartment":
    price = 35.00 * days
    if days < 10:
        price = price - (price * 0.1)
    elif 10 <= days <= 15:
        price = price - (price * 0.15)
    elif days > 15:
        price = price - (price * 0.20)
elif room_type == "room for one person":
    price = 18.00 * days

if score == "positive":
    price = price + (price * 0.25)
elif score == "negative":
    price = price - (price * 0.10)

print(f"{price:.2f}")






