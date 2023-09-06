nums = [int(x) for x in input().split(', ')]

groups = {}

bounty = 10

while nums:
    curr = [n for n in nums if n <= bounty]
    [nums.remove(n) for n in curr]
    groups[bounty] = curr
    bounty += 10


for group, items in groups.items():
    print(f"Group of {group}'s: {items}")
