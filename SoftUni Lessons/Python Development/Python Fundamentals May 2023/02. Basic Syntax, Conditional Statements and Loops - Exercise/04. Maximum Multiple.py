divisor = int(input())
boundary = int(input())

for num in range(boundary, 0, -1):
    if num % divisor == 0:
        print(num)
        break
