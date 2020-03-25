def even_numbers(function):
    def wrapper(numbers):
        numbers = [num for num in numbers if num % 2 == 0]
        return numbers
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))  # Expected output: [2, 4]
