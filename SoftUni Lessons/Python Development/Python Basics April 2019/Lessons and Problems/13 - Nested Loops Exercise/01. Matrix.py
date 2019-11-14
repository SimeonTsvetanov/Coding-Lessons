a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x1 in range(a, b + 1):
    for x2 in range(a, b + 1):
        for x3 in range(c, d + 1):
            for x4 in range(c, d + 1):
                if (x1 + x4) == (x2 + x3) and x1 != x2 and x3 != x4:
                    print(f"{x1}{x2}")
                    print(f"{x3}{x4}")
                    print()
