month = input()
time_hours = int(input())
people = int(input())
time_of_day = input()

price_hour = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price_hour = 10.5
    elif time_of_day == "night":
        price_hour = 8.4
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price_hour = 12.6
    elif time_of_day == "night":
        price_hour = 10.2

if people >= 4:
    price_hour -= price_hour * 0.1
if time_hours >= 5:
    price_hour -= price_hour * 0.5

print(f"Price per person for one hour: {price_hour:.2f}")
print(f"Total cost of the visit: {((price_hour * time_hours) * people):.2f}")
