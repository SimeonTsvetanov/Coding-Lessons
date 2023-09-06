def orders(product, count):
    prices = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }

    total = prices[product] * count
    return f"{total:.2f}"


print(orders(input(), int(input())))

