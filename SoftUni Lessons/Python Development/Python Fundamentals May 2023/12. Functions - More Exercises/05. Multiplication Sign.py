def multiplication_sign():
    a, b, c = int(input()), int(input()), int(input())
    negatives = sum(1 for num in [a, b, c] if num < 0)

    # If any number is zero, the result will be zero
    if 0 in [a, b, c]:
        return "zero"

    # If there are an odd number of negative numbers, the result will be negative
    if negatives % 2 == 1:
        return "negative"

    # If there are an even number of negative numbers, the result will be positive
    return "positive"


if __name__ == '__main__':
    print(multiplication_sign())
