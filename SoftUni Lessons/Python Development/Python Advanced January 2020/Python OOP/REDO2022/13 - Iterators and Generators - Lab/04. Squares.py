def squares(num):
    for i in range(1, num + 1):
        num = i * i
        yield num


print(list(squares(5)))

