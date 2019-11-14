num = int(input())

total = 0
max_number = -999999999999999999999999999999

for i in range(1, num + 1):
    in_number = int(input())
    total += in_number
    if in_number > max_number:
        max_number = in_number

total_minus_max = total - max_number

if total_minus_max == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(total_minus_max - max_number)}")

