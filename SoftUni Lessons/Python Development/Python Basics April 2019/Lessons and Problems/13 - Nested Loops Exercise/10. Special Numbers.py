n = int(input())

for i in range(1111, 10000):
    num = str(i)
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    num4 = int(num[3])
    if num1 == 0 or num2 == 0 or num3 == 0 or num4 == 0:
        continue
    if n % num1 == 0 and n % num2 == 0 and n % num3 == 0 and n % num4 == 0:
        print(i, end=" ")
