for num in range(1, int(input()) + 1):
    sumDigits = sum([int(digit) for digit in str(num)])
    special = True if sumDigits in [5, 7, 11] else False
    print(f"{num} -> {special}")
