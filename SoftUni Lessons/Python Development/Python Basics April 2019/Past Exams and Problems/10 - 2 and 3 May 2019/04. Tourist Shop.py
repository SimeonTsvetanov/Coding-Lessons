budget = float(input())

command = input()

counter = 0
total = 0

while command != "Stop":
    product_price = float(input())
    counter += 1
    if counter % 3 == 0:
        product_price *= 0.5
    if product_price > budget:
        print("You don't have enough money!")
        print(f"You need {(product_price - budget):.2f} leva!")
        break
    budget -= product_price
    total += product_price
    command = input()

if command == "Stop":
    print(f"You bought {counter} products for {total:.2f} leva.")
