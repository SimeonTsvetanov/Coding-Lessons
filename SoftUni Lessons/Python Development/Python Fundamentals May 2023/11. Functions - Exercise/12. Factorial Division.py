def factorial_division(a, b):
    def factorial(n):
        if n == 0:
            return 1

        return n * factorial(n - 1)

    return f"{factorial(a) / factorial(b):.2f}"


print(factorial_division(int(input()), int(input())))
