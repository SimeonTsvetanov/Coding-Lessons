import math

budget = float(input())
floor_width = float(input())
floor_length = float(input())
triangle_side = float(input())
triangle_height = float(input())
one_tile_price = float(input())
work_price = float(input())

floor_area = floor_width * floor_length
triangle_area = triangle_side * triangle_height / 2
needed_tiles = math.ceil(floor_area / triangle_area) + 5
total_price = needed_tiles * one_tile_price + work_price

if total_price <= budget:
    print(f"{(budget - total_price):.2f} lv left.")
else:
    print(f"You'll need {abs(total_price - budget):.2f} lv more.")
