chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

flowers = roses + tulips + chrysanthemums
price = 0

if season == "Spring" or season == "Summer":
    price = (2.00 * chrysanthemums) + (4.10 * roses) + (2.50 * tulips)
elif season == "Autumn" or season == "Winter":
    price = (3.75 * chrysanthemums) + (4.50 * roses) + (4.15 * tulips)

if holiday == "Y":
    price += price * 0.15

if tulips > 7 and season == "Spring":
    price -= price * 0.05
if roses >= 10 and season == "Winter":
    price -= price * 0.1
if flowers > 20:
    price -= price * 0.2

price += 2

print(f"{price:.2f}")

