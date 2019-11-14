parts = int(input())
price_one_point = float(input())

total_points = 0

for i in range(1, parts + 1):
    points = int(input())
    if i % 2 == 0:
        total_points += points * 2
    else:
        total_points += points

print(f"The project prize was {(total_points * price_one_point):.2f} lv.")
