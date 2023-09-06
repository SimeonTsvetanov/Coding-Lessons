def data_types(type_of_data, data):
    run = {
        'int': (lambda i: int(i) * 2),
        'real': (lambda f: f"{(float(f) * 1.5):.2f}"),
        'string': (lambda s: f"${s}$"),
    }

    print(run[type_of_data](data))


data_types(input(), input())
