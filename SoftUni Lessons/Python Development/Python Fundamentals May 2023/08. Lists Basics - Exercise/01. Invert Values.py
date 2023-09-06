nums = [abs(int(num)) if int(num) < 0 else (-int(num))for num in input().split(' ')]
print(nums)

