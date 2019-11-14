import math
n = int(input())
ll = int(input())

for x1 in range(1, n):
    for x2 in range(1, n):
        for x3 in range(97, ll + 97):
            for x4 in range(97, ll + 97):
                if x1 > x2:
                    b = x1
                else:
                    b = x2
                for x5 in range(b + 1, n + 1):
                    print(f"{x1}{x2}{chr(x3)}{chr(x4)}{x5}", end=" ")





