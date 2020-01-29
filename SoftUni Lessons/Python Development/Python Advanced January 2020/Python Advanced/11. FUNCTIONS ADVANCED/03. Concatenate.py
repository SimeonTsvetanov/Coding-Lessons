def concatenate(*args):
    result = ""
    for string in args:
        result += string
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
