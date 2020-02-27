def fix_calendar(nums):
    swap = False
    while not swap:
        swap = True
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                swap = False
    return nums


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
