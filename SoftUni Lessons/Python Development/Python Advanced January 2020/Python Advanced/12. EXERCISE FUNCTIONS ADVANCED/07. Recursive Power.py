def recursive_power(number, power):
    if True:
        if power == 1:
            return number
        return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
