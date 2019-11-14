import math

price_tennis_rocket = float(input())
count_tennis_rockets = int(input())
count_kicks = int(input())

total_rockets = price_tennis_rocket * count_tennis_rockets
total_kicks = (price_tennis_rocket / 6) * count_kicks
total_extra = (total_rockets + total_kicks) * 0.2
total = total_rockets + total_kicks + total_extra

own = total / 8
sponsor = total * 7 / 8

print(f"Price to be paid by Djokovic {math.floor(own)}")
print(f"Price to be paid by sponsors {math.ceil(sponsor)}")
