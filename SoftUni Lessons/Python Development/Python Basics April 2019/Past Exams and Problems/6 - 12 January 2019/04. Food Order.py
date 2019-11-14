budget = float(input())

command = None
items = 0
price = 2.5
amount = 0

while command != "Order":
    command = input()
    if command == "Order":
        break
    items += 1
    amount = float(input())
    price += amount
    if price > budget:
        print("You will exceed the budget if you order this!")
        price -= amount
        items -= 1
        continue

print(f"You ordered {items} items!")
print(f"Total: {price:.2f}")
