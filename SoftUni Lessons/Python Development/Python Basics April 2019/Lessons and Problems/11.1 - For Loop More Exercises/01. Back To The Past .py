heritage = float(input())
goal_year = int(input())

age = 18

for year in range(1800, goal_year + 1):
    if year % 2 == 0:
        heritage -= 12000
        age += 1
    if year % 2 != 0:
        heritage -= 12000 + (50 * age)
        age += 1

if heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage):.2f} dollars to survive.")
