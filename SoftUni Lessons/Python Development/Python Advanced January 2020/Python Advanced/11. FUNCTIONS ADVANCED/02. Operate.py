def operate(operator, *args):
    result = 1 if operator == "*" or operator == "/" else 0
    for num in args:
        result = eval(f"{result} {operator} {num}")
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
