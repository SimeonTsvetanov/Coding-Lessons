nums = [int(num) for num in input().split(', ')]
beggars = [0 for _ in range(int(input()))]

beggar = 0

while nums:
    beggars[beggar] += nums.pop(0)
    beggar += 1
    if beggar == len(beggars):
        beggar = 0

print(beggars)
