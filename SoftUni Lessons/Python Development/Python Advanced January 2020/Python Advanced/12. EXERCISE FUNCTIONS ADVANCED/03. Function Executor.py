# This is my code:
"""
def func_executor(*args):
    result = []
    for code in args:
        function = code[0]
        nums = code[1]
        result.append(function(*nums))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
"""


def func_executor(*args):
    """this is the solution from for in class"""
    results = []
    for arg in args:
        func = arg[0]
        params = arg[1]
        results.append(func(*params))
    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
