nums = [int(n) for n in input().split(', ')]
zeroes = []
while 0 in nums:
    nums.remove(0)
    zeroes.append(0)

nums.extend(zeroes)
print(nums)

