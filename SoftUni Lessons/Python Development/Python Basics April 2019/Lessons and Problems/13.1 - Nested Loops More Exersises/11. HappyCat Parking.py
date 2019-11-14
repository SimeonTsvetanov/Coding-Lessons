count_days = int(input())
count_hours = int(input())

total = 0
daily_total = 0

for day in range(1, count_days + 1):
    for hour in range(1, count_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            daily_total += 2.5
            total += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            daily_total += 1.25
            total += 1.25
        else:
            daily_total += 1
            total += 1
    print(f"Day: {day} - {daily_total:.2f} leva")
    daily_total = 0

print(f"Total: {total:.2f} leva")