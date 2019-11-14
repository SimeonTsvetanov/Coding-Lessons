budget = float(input())
count_tv_series = int(input())

total_price = 0

for serial in range(count_tv_series):
    name_serial = input()
    price_serial = float(input())
    if name_serial == "Thrones":
        total_price += (price_serial * 0.5)
    elif name_serial == "Lucifer":
        total_price += (price_serial * 0.6)
    elif name_serial == "Protector":
        total_price += (price_serial * 0.7)
    elif name_serial == "TotalDrama":
        total_price += (price_serial * 0.8)
    elif name_serial == "Area":
        total_price += (price_serial * 0.9)
    else:
        total_price += price_serial

if budget >= total_price:
    print(f"You bought all the series and left with {(budget - total_price):.2f} lv.")
else:
    print(f"You need {(total_price - budget):.2f} lv. more to buy the series!")
