n = int(input())
m = int(input())
s = int(input())

for i in range(m, n - 1, -1):
    if i % 3 == 0 and i % 2 == 0:
        if i == s:
            break
        print(i, end=' ')
    else:
        continue


