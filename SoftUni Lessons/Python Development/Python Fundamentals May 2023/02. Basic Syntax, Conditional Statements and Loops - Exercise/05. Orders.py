total = 0
for order in range(int(input())):
    price = float(input())
    days = int(input())
    needed = int(input())

    if not ((0.01 <= price <= 100) and (1 <= days <= 31) and (1 <= needed <= 2000)):
        continue
    print(f"The price for the coffee is: ${(price * days * needed):.2f}")
    total += price * days * needed

print(f"Total: ${total:.2f}")
