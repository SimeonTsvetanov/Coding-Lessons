def odd_and_even_sum(num):
    odd_sum = sum(list(filter(lambda x: x % 2 != 0, list(map(int, list(str(num)))))))
    even_sum = sum(list(filter(lambda x: x % 2 == 0, list(map(int, list(str(num)))))))

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_and_even_sum(int(input())))
