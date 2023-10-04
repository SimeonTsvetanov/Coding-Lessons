"""
Write a function called multiply that can receive any quantity of numbers (integers) as different parameters
and returns the result of the multiplication of all of them.
Submit only your function in the Judge system.
"""


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(1, 4, 5))           # 20
print(multiply(4, 5, 6, 1, 3))     # 360
print(multiply(2, 0, 1000, 5000))  # 0
