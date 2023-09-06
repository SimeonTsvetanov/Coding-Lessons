nums = [int(num) for num in input().split()]
k = int(input())

result = []

current_index = 0

while nums:
    current_index += k - 1
    if current_index < len(nums):
        result.append(nums[current_index])
        nums.pop(current_index)

    else:
        current_index = current_index % len(nums)
        result.append(nums[current_index])
        nums.pop(current_index)

print(f"[{','.join([str(n) for n in result])}]")