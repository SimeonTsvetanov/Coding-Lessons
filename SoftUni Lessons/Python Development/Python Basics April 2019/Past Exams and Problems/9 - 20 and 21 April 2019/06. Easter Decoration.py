count_customers = int(input())

order = None

current_total = 0
current_count_orders = 0

total = 0

for customer in range(count_customers):
    while True:
        order = input()
        if order == "Finish":
            break
        current_count_orders += 1
        if order == "basket":
            current_total += 1.5
        elif order == "wreath":
            current_total += 3.8
        elif order == "chocolate bunny":
            current_total += 7
    if current_count_orders % 2 == 0:
        current_total -= current_total * 0.2
    print(f"You purchased {current_count_orders} items for {current_total:.2f} leva.")
    total += current_total
    current_count_orders = 0
    current_total = 0

print(f"Average bill per client is: {(total / count_customers):.2f} leva.")

