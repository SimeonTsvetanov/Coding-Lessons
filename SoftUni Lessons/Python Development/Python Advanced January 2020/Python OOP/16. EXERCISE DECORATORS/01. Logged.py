def logged(function):
    def wrapper(*args):
        result = ''
        result += f'you called {function.__name__}{args}\n'
        func_result = function(*args)
        result += f'it returned {func_result}'
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
