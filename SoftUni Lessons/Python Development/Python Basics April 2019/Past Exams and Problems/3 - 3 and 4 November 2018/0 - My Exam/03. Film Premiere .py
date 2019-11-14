name = input()
packet = input()
count = int(input())

price = 0

if name == "John Wick":
    if packet == "Drink":
        price = count * 12
    elif packet == "Popcorn":
        price = count * 15
    elif packet == "Menu":
        price = count * 19
elif name == "Star Wars":
    if packet == "Drink":
        price = count * 18
    elif packet == "Popcorn":
        price = count * 25
    elif packet == "Menu":
        price = count * 30
elif name == "Jumanji":
    if packet == "Drink":
        price = count * 9
    elif packet == "Popcorn":
        price = count * 11
    elif packet == "Menu":
        price = count * 14

if name == "Star Wars" and count >= 4:
    price -= price * 0.3
if name == "Jumanji" and count == 2:
    price -= price * 0.15

print(f"Your bill is {price:.2f} leva.")
