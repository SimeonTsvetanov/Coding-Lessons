products = {}

while True:
    command = input().split(': ')
    if command[0] == "statistics":
        break
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
