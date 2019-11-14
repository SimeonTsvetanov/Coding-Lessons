type_final = input()
type_ticket = input()
count_tickets = int(input())
trophy_pic = input()

price = 0

if type_final == "Quarter final":
    if type_ticket == "Standard":
        price = 55.50 * count_tickets
    elif type_ticket == "Premium":
        price = 105.20 * count_tickets
    elif type_ticket == "VIP":
        price = 118.90 * count_tickets
elif type_final == "Semi final":
    if type_ticket == "Standard":
        price = 75.88 * count_tickets
    elif type_ticket == "Premium":
        price = 125.22 * count_tickets
    elif type_ticket == "VIP":
        price = 300.40 * count_tickets
elif type_final == "Final":
    if type_ticket == "Standard":
        price = 110.10 * count_tickets
    elif type_ticket == "Premium":
        price = 160.66 * count_tickets
    elif type_ticket == "VIP":
        price = 400 * count_tickets

if 2500 < price <= 4000:
    price -= price * 0.1
if price > 4000:
    price -= price * 0.25
    trophy_pic = "N"

if trophy_pic == "Y":
    price += 40 * count_tickets

print(f"{price:.2f}")


