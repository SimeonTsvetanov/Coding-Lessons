year_contract = input()
type_contract = input()
added_dessert = input()
count_months = int(input())

price = 0

if year_contract == "one":
    if type_contract == "Small":
        price = 9.98
    elif type_contract == "Middle":
        price = 18.99
    elif type_contract == "Large":
        price = 25.98
    elif type_contract == "ExtraLarge":
        price = 35.99
elif year_contract == "two":
    if type_contract == "Small":
        price = 8.58
    elif type_contract == "Middle":
        price = 17.09
    elif type_contract == "Large":
        price = 23.59
    elif type_contract == "ExtraLarge":
        price = 31.79

if added_dessert == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if year_contract == "two":
    price -= price * 0.0375

price = price * count_months

print(f"{price:.2f} lv.")





