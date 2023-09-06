def perfect_number(num):
    if sum([i for i in range(1, num) if num % i == 0]) == num:
        return f'We have a perfect number!'
    else:
        return "It's not so perfect."


print(perfect_number(int(input())))
