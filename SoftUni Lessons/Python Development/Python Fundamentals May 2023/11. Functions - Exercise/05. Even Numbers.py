def even_numbers(nums):
    even_nums = list(filter(lambda x: x % 2 == 0, list(map(int, nums.split(' ')))))
    return even_nums


print(even_numbers(input()))
