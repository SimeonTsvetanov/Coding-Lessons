tax = int(input())

price_kicks = tax - tax * 0.4
price_wear = price_kicks - price_kicks * 0.2
price_ball = price_wear / 4
price_extra = price_ball / 5

total = price_kicks + price_wear + price_ball + price_extra + tax

print(f"{total:.2f}")

