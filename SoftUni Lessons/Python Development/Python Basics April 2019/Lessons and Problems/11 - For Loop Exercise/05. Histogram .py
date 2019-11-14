count_numbers = int(input())

under_200 = 0
between_200_399 = 0
between_400_599 = 0
between_600_799 = 0
bigger_then_800 = 0

for i in range(0, count_numbers):
    number = int(input())
    if number < 200:
        under_200 += 1
    elif 200 <= number <= 399:
        between_200_399 += 1
    elif 400 <= number <= 599:
        between_400_599 += 1
    elif 600 <= number <= 799:
        between_600_799 += 1
    elif number >= 800:
        bigger_then_800 += 1

print(f"{(under_200 / count_numbers * 100):.2f}%")
print(f"{(between_200_399 / count_numbers * 100):.2f}%")
print(f"{(between_400_599 / count_numbers * 100):.2f}%")
print(f"{(between_600_799 / count_numbers * 100):.2f}%")
print(f"{(bigger_then_800 / count_numbers * 100):.2f}%")

