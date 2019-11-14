budget = float(input())
season = input()

class_car = None
car = None
price = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.8
elif budget > 500:
    class_car = "Luxury class"
    car = "Jeep"
    price = budget * 0.9

print(class_car)
print(f"{car} - {price:.2f}")
