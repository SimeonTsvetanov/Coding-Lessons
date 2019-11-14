count_chrysanthemums = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
if_holiday = input()

total = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00 * count_chrysanthemums
    roses_price = 4.10 * count_roses
    tulips_price = 2.50 * count_tulips
    total = chrysanthemums_price + roses_price + tulips_price
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75 * count_chrysanthemums
    roses_price = 4.50 * count_roses
    tulips_price = 4.15 * count_tulips
    total = chrysanthemums_price + roses_price + tulips_price

if if_holiday == "Y":
    total += total * 0.15

if season == "Spring" and count_tulips > 7:
    total -= total * 0.05
if season == "Winter" and count_roses >= 10:
    total -= total * 0.1
if (count_chrysanthemums + count_roses + count_tulips) > 20:
    total -= total * 0.2

total = total + 2

print(f"{total:.2f}")


