budget = float(input())

command = None
type_deco = None
count_deco = 0
price = 0
count_balloons = 0
count_flowers = 0
count_candles = 0
count_ribbon = 0

while not(budget <= price):
    type_deco = input()
    if type_deco == "stop":
        break
    count_deco = int(input())
    if type_deco == "balloons":
        count_balloons += count_deco
        price += 0.1 * count_deco
    elif type_deco == "flowers":
        count_flowers += count_deco
        price += 1.5 * count_deco
    elif type_deco == "candles":
        count_candles += count_deco
        price += 0.5 * count_deco
    elif type_deco == "ribbon":
        count_ribbon += count_deco
        price += 2 * count_deco

if type_deco == "stop":
    print(f"Spend money: {price:.2f}")
    print(f"Money left: {(budget - price):.2f}")
if budget <= price:
    print("All money is spent!")
print(f"Purchased decoration is {count_balloons} balloons, {count_ribbon} m ribbon, {count_flowers} flowers"
      f" and {count_candles} candles.")
