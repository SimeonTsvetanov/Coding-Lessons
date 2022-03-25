def shopping_list(budget, **args):
    result = ''
    count_items = 5
    if budget < 100:
        return f"You do not have enough budget."

    for product, values in args.items():
        if count_items == 0:
            break
        price, quantity = values[0], values[1]
        total = price * quantity
        if (budget >= total) and (count_items - 1 >= 0):
            budget -= total
            count_items -= 1
            result += f"You bought {product} for {total:.2f} leva.\n"
    return result.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


