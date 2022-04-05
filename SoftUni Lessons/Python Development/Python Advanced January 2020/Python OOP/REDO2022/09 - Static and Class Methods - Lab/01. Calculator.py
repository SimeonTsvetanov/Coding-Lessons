class Calculator:
    """
    •	add(*args) - sums all the arguments passed to the function and returns the result
    •	multiply(*args) - multiplies all the numbers and returns the result
    •	divide(*args) - divides all the numbers (starting from the first one) and returns the result
    •	subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result
    """

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        args = list(args)
        res = args.pop(0)
        for num in args:
            res *= num
        return res

    @staticmethod
    def divide(*args):
        args = list(args)
        res = args.pop(0)
        for num in args:
            res = res / num
        return res

    @staticmethod
    def subtract(*args):
        args = list(args)
        res = args.pop(0)
        for num in args:
            res -= num
        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
