team = input()
stock = input()
count = int(input())

price = 0

if team == "Argentina":
    if stock == "flags":
        price = count * 3.25
    elif stock == "caps":
        price = count * 7.2
    elif stock == "posters":
        price = count * 5.1
    elif stock == "stickers":
        price = count * 1.25
    else:
        print(f"Invalid stock!")
elif team == "Brazil":
    if stock == "flags":
        price = count * 4.2
    elif stock == "caps":
        price = count * 8.5
    elif stock == "posters":
        price = count * 5.35
    elif stock == "stickers":
        price = count * 1.2
    else:
        print(f"Invalid stock!")
elif team == "Croatia":
    if stock == "flags":
        price = count * 2.75
    elif stock == "caps":
        price = count * 6.9
    elif stock == "posters":
        price = count * 4.95
    elif stock == "stickers":
        price = count * 1.1
    else:
        print(f"Invalid stock!")
elif team == "Denmark":
    if stock == "flags":
        price = count * 3.1
    elif stock == "caps":
        price = count * 6.5
    elif stock == "posters":
        price = count * 4.8
    elif stock == "stickers":
        price = count * 0.9
    else:
        print(f"Invalid stock!")
else:
    print(f"Invalid country!")

if price > 0:
    print(f"Pepi bought {count} {stock} of {team} for {price:.2f} lv.")
