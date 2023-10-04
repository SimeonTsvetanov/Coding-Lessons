def grocery_store(**kwargs):
    store = {}

    for product, value in kwargs.items():
        if product not in store:
            store[product] = 0
        store[product] += value

    to_print = ''

    for product, quantity in sorted(store.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        to_print += f"{product}: {quantity}\n"

    return to_print


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(20 * '*')

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
