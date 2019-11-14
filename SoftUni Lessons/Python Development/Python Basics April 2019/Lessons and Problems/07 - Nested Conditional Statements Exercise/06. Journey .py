budget = float(input())
season = input()

destination = None
accommodation = None
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        price = budget * 0.3
    elif season == "winter":
        accommodation = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        price = budget * 0.4
    elif season == "winter":
        accommodation = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")