budget = int(input())

result = "You bought everything needed."

while True:
    product = input()

    if product == "End":
        break

    budget -= int(product)

    if budget < 0:
        result = "You went in overdraft!"
        break

print(result)
