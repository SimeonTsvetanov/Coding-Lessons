n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + 1):
    num = str(i)
    sum_odd = int(num[0]) + int(num[2]) + int(num[4])
    sum_even = int(num[1]) + int(num[3]) + int(num[5])
    if sum_odd == sum_even:
        print(i, end=" ")

