n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, n):
    num_for_left = float(input())
    left_sum += num_for_left

for i in range(0, n):
    num_for_right = int(input())
    right_sum += num_for_right

if left_sum == right_sum:
    print(f"Yes, sum = {int(left_sum)}")
else:
    print(f"No, diff = {int(abs(left_sum - right_sum))}")
