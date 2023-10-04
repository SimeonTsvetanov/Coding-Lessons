chocolates = [int(n) for n in input().split(', ')]
cups = [int(n) for n in input().split(', ')]

milkshakes = 0

while (milkshakes != 5) and cups and chocolates:

    if chocolates[-1] <= 0:
        chocolates.pop(-1)
        continue

    if cups[0] <= 0:
        cups.pop(0)
        continue

    chocolate = chocolates.pop(-1)
    cup = cups.pop(0)

    if chocolate == cup:
        milkshakes += 1
    else:
        cups.append(cup)
        chocolates.insert(1, chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if len(chocolates) >= 1:
    print(f"Chocolate: {', '.join([str(c) for c in chocolates])}")
else:
    print("Chocolate: empty")

if len(cups) >= 1:
    print(f"Milk: {', '.join([str(c) for c in cups])}")
else:
    print("Milk: empty")
