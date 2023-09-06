items = [i for i in input().split('|')]
budget = float(input())
sold_items = []
profit = 0

for i in items:
    item = i.split('->')[0]
    price = float(i.split('->')[1])
    if item == 'Clothes' and price <= 50 or item == 'Shoes' and price <= 35 or item == 'Accessories' and price <= 20.50:
        if budget - price >= 0:
            budget -= price
            sold_items.append(price * 1.4)
            profit += price * 1.4 - price

print(' '.join([str(f"{item:.2f}") for item in sold_items]))
print(f"Profit: {profit:.2f}")
print(f"Hello, France!") if budget + sum(sold_items) >= 150 else print("Not enough money.")


# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120

# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90
