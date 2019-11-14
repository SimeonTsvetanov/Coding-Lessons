import math
type_sushi = input()
name_restaurant = input()
count_portions = int(input())
deliver = input()

price = 0

if name_restaurant == "Sushi Zone":
    if type_sushi == "sashimi":
        price = count_portions * 4.99
    elif type_sushi == "maki":
        price = count_portions * 5.29
    elif type_sushi == "uramaki":
        price = count_portions * 5.99
    elif type_sushi == "temaki":
        price = count_portions * 4.29
elif name_restaurant == "Sushi Time":
    if type_sushi == "sashimi":
        price = count_portions * 5.49
    elif type_sushi == "maki":
        price = count_portions * 4.69
    elif type_sushi == "uramaki":
        price = count_portions * 4.49
    elif type_sushi == "temaki":
        price = count_portions * 5.19
elif name_restaurant == "Sushi Bar":
    if type_sushi == "sashimi":
        price = count_portions * 5.25
    elif type_sushi == "maki":
        price = count_portions * 5.55
    elif type_sushi == "uramaki":
        price = count_portions * 6.25
    elif type_sushi == "temaki":
        price = count_portions * 4.75
elif name_restaurant == "Asian Pub":
    if type_sushi == "sashimi":
        price = count_portions * 4.5
    elif type_sushi == "maki":
        price = count_portions * 4.8
    elif type_sushi == "uramaki":
        price = count_portions * 5.5
    elif type_sushi == "temaki":
        price = count_portions * 5.5
else:
    print(f"{name_restaurant} is invalid restaurant!")

if deliver == "Y":
    price += price * 0.2

total = math.ceil(price)

if price > 0:
    print(f"Total price: {total} lv.")
