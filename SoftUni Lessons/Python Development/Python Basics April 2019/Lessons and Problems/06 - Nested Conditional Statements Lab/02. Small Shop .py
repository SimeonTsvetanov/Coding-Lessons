product = input().lower()
city = input().lower()
volume = float(input())

if city == "sofia":
    if product == "coffee":
        print(volume * 0.50)
    if product == "water":
        print(volume * 0.80)
    if product == "beer":
        print(volume * 1.20)
    if product == "sweets":
        print(volume * 1.45)
    if product == "peanuts":
        print(volume * 1.60)
if city == "plovdiv":
    if product == "coffee":
        print(volume * 0.40)
    if product == "water":
        print(volume * 0.70)
    if product == "beer":
        print(volume * 1.15)
    if product == "sweets":
        print(volume * 1.30)
    if product == "peanuts":
        print(volume * 1.50)
if city == "varna":
    if product == "coffee":
        print(volume * 0.45)
    if product == "water":
        print(volume * 0.70)
    if product == "beer":
        print(volume * 1.10)
    if product == "sweets":
        print(volume * 1.35)
    if product == "peanuts":
        print(volume * 1.55)

