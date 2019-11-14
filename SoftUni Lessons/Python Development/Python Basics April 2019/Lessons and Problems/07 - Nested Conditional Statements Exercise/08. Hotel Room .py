month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50 * nights
    apartment = 65 * nights
    if 7 < nights <= 14:
        studio -= studio * 0.05
    elif nights > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1
elif month == "June" or month == "September":
    studio = 75.20 * nights
    apartment = 68.70 * nights
    if nights > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
elif month == "July" or month == "August":
    studio = 76 * nights
    apartment = 77 * nights
    if nights > 14:
        apartment -= apartment * 0.1

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")

