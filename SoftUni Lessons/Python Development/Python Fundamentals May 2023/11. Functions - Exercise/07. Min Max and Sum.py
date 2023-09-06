def min_max_and_sum(nums):
    nums = [int(num) for num in nums.split(' ')]
    return f"The minimum number is {min(nums)}\nThe maximum number is {max(nums)}\nThe sum number is: {sum(nums)}"


print(min_max_and_sum(input()))
