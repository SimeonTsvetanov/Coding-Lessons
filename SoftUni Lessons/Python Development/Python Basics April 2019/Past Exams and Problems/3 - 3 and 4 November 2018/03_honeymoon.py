budget = float(input())
city = input()
nights = int(input())

price_night = 0
price_tickets = 0

if city == "Cairo":
    price_night = 250
    price_tickets = 600
elif city == "Paris":
    price_night = 150
    price_tickets = 350
elif city == "Lima":
    price_night = 400
    price_tickets = 850
elif city == "New York":
    price_night = 300
    price_tickets = 650
elif city == "Tokyo":
    price_night = 350
    price_tickets = 700

price_nights = (price_night * nights * 2) + price_tickets

if 1 <= nights <= 4:
    if city == "Cairo" or city == "New York":
        price_nights -= price_nights * 0.03
elif 5 <= nights <= 9:
    if city == "Cairo" or city == "New York":
        price_nights -= price_nights * 0.05
    elif city == "Paris":
        price_nights -= price_nights * 0.07
elif 10 <= nights <= 24:
    if city == "Cairo":
        price_nights -= price_nights * 0.1
    elif city == "Paris" or city == "New York" or city == "Tokyo":
        price_nights -= price_nights * 0.12
elif 25 <= nights <= 49:
    if city == "Tokyo" or city == "Cairo":
        price_nights -= price_nights * 0.17
    elif city == "New York" or city == "Lima":
        price_nights -= price_nights * 0.19
    elif city == "Paris":
        price_nights -= price_nights * 0.22
elif nights >= 50:
    price_nights -= price_nights * 0.3

if budget >= price_nights:
    print(f"Yes! You have {(budget - price_nights):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price_nights - budget):.2f} leva.")
