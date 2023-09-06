budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) / 4
eggs = 0
bread = 0

while True:
    price = price_flour + price_eggs + price_milk
    if budget - price >= 0:
        # make the bread
        budget -= price
        bread += 1
        eggs += 3
        if bread % 3 == 0:
            eggs -= (bread - 2)
    else:
        # not enough money kill the program
        print(f"You made {bread} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
        break
