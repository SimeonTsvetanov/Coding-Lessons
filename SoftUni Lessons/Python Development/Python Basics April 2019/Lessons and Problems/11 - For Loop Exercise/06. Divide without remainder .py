count_numbers = int(input())

reminder_2 = 0
reminder_3 = 0
reminder_4 = 0

for i in range(0, count_numbers):
    number = int(input())
    if number % 2 == 0:
        reminder_2 += 1
    if number % 3 == 0:
        reminder_3 += 1
    if number % 4 == 0:
        reminder_4 += 1

print(f"{(reminder_2 / count_numbers * 100):.2f}%")
print(f"{(reminder_3 / count_numbers * 100):.2f}%")
print(f"{(reminder_4 / count_numbers * 100):.2f}%")