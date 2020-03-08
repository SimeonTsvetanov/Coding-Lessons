def execute(function, *args):
    return function(*args)


def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")


def say_bye(name):
    print(f"Bye, {name}")


def test_func(name, age):
    return f"I am {name} and I am {age} years old"


execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
execute(test_func, "Tanya", 22)

