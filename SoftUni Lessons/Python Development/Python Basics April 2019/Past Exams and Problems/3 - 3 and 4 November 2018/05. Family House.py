months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

average_total = 0

for i in range(months):
    current_electricity = float(input())
    total_electricity += current_electricity
    current_water = 20
    total_water += current_water
    current_internet = 15
    total_internet += current_internet
    current_other = (current_electricity + current_water + current_internet) + \
                    ((current_electricity + current_water + current_internet) * 0.2)
    total_other += current_other
    average_total += current_electricity + current_water + current_internet + current_other

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {(average_total / months):.2f} lv")
