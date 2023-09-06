import math
nums = [int(num) for num in input().split(' ')]
[nums.remove(min(nums)) for _ in range(int(input()))]
print(', '.join([str(n) for n in nums]))
