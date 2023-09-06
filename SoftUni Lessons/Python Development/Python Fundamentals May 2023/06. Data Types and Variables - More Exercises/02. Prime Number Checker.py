def is_prime(n):
    if n < 2:  # 1, 0 and all negative numbers are not prime
        return False
    elif n == 2:  # 2 is prime but cannot be calculated with the formula below because of the range function
        return True
    else:
        for i in range(2, n):
            if (n % i) == 0:  # if you can precisely divide a number by another number, it is not prime
                return False
        return True


print(is_prime(int(input())))
