data = input().split(' ')

bakery = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])
    bakery[product] = quantity

print(bakery)
