def tags(tag):
    def decorator(function):
        def wrapper(*args):
            func_return = function(*args)
            result = f"<{tag}>{func_return}</{tag}>"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
# Expected Output: <p>Hello you!</p>


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
# Expected Output: <h1>HELLO</h1>
