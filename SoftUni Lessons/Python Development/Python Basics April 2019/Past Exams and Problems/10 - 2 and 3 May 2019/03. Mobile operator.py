contract_years = input()
contract_type = input()
internet = input()
months = int(input())

month_price = 0

if contract_years == "one":
    if contract_type == "Small":
        month_price = 9.98
    elif contract_type == "Middle":
        month_price = 18.99
    elif contract_type == "Large":
        month_price = 25.98
    elif contract_type == "ExtraLarge":
        month_price = 35.99
elif contract_years == "two":
    if contract_type == "Small":
        month_price = 8.58
    elif contract_type == "Middle":
        month_price = 17.09
    elif contract_type == "Large":
        month_price = 23.59
    elif contract_type == "ExtraLarge":
        month_price = 31.79

if internet == "yes":
    if month_price <= 10:
        month_price += 5.5
    elif month_price <= 30:
        month_price += 4.35
    elif month_price > 30:
        month_price += 3.85

total = month_price * months

if contract_years == "two":
    total -= total * 0.0375

print(f"{total:.2f} lv.")
