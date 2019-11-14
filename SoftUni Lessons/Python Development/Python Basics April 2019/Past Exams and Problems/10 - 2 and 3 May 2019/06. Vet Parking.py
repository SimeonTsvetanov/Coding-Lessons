days = int(input())
hours = int(input())

current_hour_rate = 0
total = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_hour_rate += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            current_hour_rate += 1.25
        else:
            current_hour_rate += 1
    print(f"Day: {day} - {current_hour_rate:.2f} leva")
    total += current_hour_rate
    current_hour_rate = 0

print(f"Total: {total:.2f} leva")
