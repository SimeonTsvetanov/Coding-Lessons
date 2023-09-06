def calculator(operator, num1, num2):
    calc = {
        'add': (lambda a, b: a + b),
        'subtract': (lambda a, b: a - b),
        'multiply': (lambda a, b: a * b),
        'divide': (lambda a, b: int(a / b))
    }

    return calc[operator](num1, num2)


print(calculator(input(), int(input()), int(input())))


# print(calculator('subtract', 5, 4))  # 1
# print(calculator('divide', 8, 4))  # 2

