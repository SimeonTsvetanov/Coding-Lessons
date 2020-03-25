def fibonacci():
    previous_number = 0
    current_number = 1
    yield previous_number
    yield current_number
    while True:
        next_number = previous_number + current_number
        yield next_number
        previous_number = current_number
        current_number = next_number


generator = fibonacci()
for i in range(5):
    print(next(generator))
