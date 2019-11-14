size = input()
color = input()
count = int(input())

price = 0

if size == "Large":
    if color == "Red":
        price = count * 16
    elif color == "Green":
        price = count * 12
    elif color == "Yellow":
        price = count * 9
elif size == "Medium":
    if color == "Red":
        price = count * 13
    elif color == "Green":
        price = count * 9
    elif color == "Yellow":
        price = count * 7
elif size == "Small":
    if color == "Red":
        price = count * 9
    elif color == "Green":
        price = count * 8
    elif color == "Yellow":
        price = count * 5

price -= price * 0.35

print(f"{price:.2f} leva.")
