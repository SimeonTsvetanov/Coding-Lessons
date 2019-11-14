import math

days_gone = int(input())
food_left = int(input())
food_day_dog_one_kg = float(input())
food_day_dog_two_kg = float(input())
food_day_dog_three_kg = float(input())

food_needed = (food_day_dog_one_kg + food_day_dog_two_kg + food_day_dog_three_kg) * days_gone

if food_left >= food_needed:
    print(f"{math.floor(food_left-food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(food_needed - food_left)} more kilos of food are needed.")
