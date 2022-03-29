def numbers_searching(*nums):
    dublicates = []
    missing_number = -111111111111
    for num in nums:
        if nums.count(num) > 1 and num not in dublicates:
            dublicates.append(num)
    min_num = min(nums)
    max_num = max(nums)
    for num in range(min_num, max_num):
        if num not in nums and num >= missing_number:
            missing_number = num

    return [missing_number, sorted(dublicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))