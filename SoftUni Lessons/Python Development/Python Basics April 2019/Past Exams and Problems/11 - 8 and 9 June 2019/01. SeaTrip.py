money_food_one_day = float(input())
money_toys_one_day = float(input())
money_hotel = float(input())

money_fuel = 54.39
money_food_and_toys = (3 * money_food_one_day) + (3 * money_toys_one_day)

day_one_hotel = money_hotel * 0.9
day_two_hotel = money_hotel * 0.85
day_three_hotel = money_hotel * 0.8

total = money_fuel + money_food_and_toys + day_one_hotel + day_two_hotel + day_three_hotel

print(f"Money needed: {total:.2f}")
