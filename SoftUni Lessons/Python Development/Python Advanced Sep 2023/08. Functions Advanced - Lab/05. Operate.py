def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
        return result
    elif operator == "/":
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result
    else:
        raise ValueError("Unknown operator: {}".format(operator))
