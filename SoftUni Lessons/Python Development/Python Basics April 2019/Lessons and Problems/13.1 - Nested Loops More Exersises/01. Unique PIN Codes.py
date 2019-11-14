n1 = int(input())
n2 = int(input())
n3 = int(input())

for x1 in range(1, n1 + 1):
    for x2 in range(1, n2 + 1):
        for x3 in range(1, n3 + 1):
            if x1 % 2 == 0 and x3 % 2 == 0:
                if x2 == 2 or x2 == 3 or x2 == 5 or x2 == 7:
                    print(f"{x1} {x2} {x3}")



