n = int(input())

num_2 = 0
num_3 = 0
num_4 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        num_2 += 1
    if num % 3 == 0:
        num_3 += 1
    if num % 4 == 0:
        num_4 += 1

print(f"{(num_2 / n * 100):.2f}%")
print(f"{(num_3 / n * 100):.2f}%")
print(f"{(num_4 / n * 100):.2f}%")
