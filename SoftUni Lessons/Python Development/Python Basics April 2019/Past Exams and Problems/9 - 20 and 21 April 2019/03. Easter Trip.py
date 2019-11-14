destination = input()
dates = input()
nights = int(input())

price = 0

if destination == "France":
    if dates == "21-23":
        price = nights * 30
    elif dates == "24-27":
        price = nights * 35
    elif dates == "28-31":
        price = nights * 40
elif destination == "Italy":
    if dates == "21-23":
        price = nights * 28
    elif dates == "24-27":
        price = nights * 32
    elif dates == "28-31":
        price = nights * 39
elif destination == "Germany":
    if dates == "21-23":
        price = nights * 32
    elif dates == "24-27":
        price = nights * 37
    elif dates == "28-31":
        price = nights * 43

print(f"Easter trip to {destination} : {price:.2f} leva.")
