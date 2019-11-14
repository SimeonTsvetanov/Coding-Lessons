n = int(input())

even_numbers_sum = 0
odd_numbers_sum = 0

for i in range(0, n):
    num = int(input())
    if i % 2 == 0:
        even_numbers_sum += num
    else:
        odd_numbers_sum += num

if even_numbers_sum == odd_numbers_sum:
    print("Yes")
    print(f"Sum = {even_numbers_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_numbers_sum - odd_numbers_sum)}")



