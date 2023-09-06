data = input().split(' ')

bakery = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])
    bakery[product] = quantity

searched = input().split(' ')

for item in searched:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
