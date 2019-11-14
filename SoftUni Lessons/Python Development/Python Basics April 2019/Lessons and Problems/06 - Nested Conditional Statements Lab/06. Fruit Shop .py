food = input().lower()
day = input().lower()
volume = float(input())

price = 0

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    if food == "banana":
        price = 2.50 * volume
        print(f"{price:.2f}")
    elif food == "apple":
        price = 1.20 * volume
        print(f"{price:.2f}")
    elif food == "orange":
        price = 0.85 * volume
        print(f"{price:.2f}")
    elif food == "grapefruit":
        price = 1.45 * volume
        print(f"{price:.2f}")
    elif food == "kiwi":
        price = 2.70 * volume
        print(f"{price:.2f}")
    elif food == "pineapple":
        price = 5.50 * volume
        print(f"{price:.2f}")
    elif food == "grapes":
        price = 3.85 * volume
        print(f"{price:.2f}")
    else:
        print("error")
elif day == "saturday" or day == "sunday":
    if food == "banana":
        price = 2.70 * volume
        print(f"{price:.2f}")
    elif food == "apple":
        price = 1.25 * volume
        print(f"{price:.2f}")
    elif food == "orange":
        price = 0.90 * volume
        print(f"{price:.2f}")
    elif food == "grapefruit":
        price = 1.60 * volume
        print(f"{price:.2f}")
    elif food == "kiwi":
        price = 3.00 * volume
        print(f"{price:.2f}")
    elif food == "pineapple":
        price = 5.60 * volume
        print(f"{price:.2f}")
    elif food == "grapes":
        price = 4.20 * volume
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")
