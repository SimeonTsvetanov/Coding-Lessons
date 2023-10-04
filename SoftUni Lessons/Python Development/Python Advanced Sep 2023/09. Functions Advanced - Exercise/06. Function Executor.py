def func_executor(*functions):
    to_print = ''
    for function, arguments in functions:
        result = function(*arguments)
        to_print += f"{function.__name__} - {result}\n"
    return to_print


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
