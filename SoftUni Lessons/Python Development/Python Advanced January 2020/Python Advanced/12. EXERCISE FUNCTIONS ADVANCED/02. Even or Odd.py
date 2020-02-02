# This is my solution
"""
def even_odd(*args):
    nums = list(args)
    even_or_odd = nums.pop()
    if even_or_odd == "even":
        return [num for num in nums if num % 2 == 0]
    else:
        return [num for num in nums if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
"""


def even_odd(*args):
    """And this is the solution from work in class"""
    x = 0 if args[-1] == "even" else 1
    return [num for num in args[:-1] if num % 2 == x]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
