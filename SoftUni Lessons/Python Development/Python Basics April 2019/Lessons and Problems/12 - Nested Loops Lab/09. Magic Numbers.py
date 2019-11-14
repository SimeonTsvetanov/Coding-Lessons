num = int(input())

for i1 in range(1, 10, 1):
    for i2 in range(1, 10, 1):
        for i3 in range(1, 10, 1):
            for i4 in range(1, 10, 1):
                for i5 in range(1, 10, 1):
                    for i6 in range(1, 10, 1):
                        combinations = i1 * i2 * i3 * i4 * i5 * i6
                        if combinations == num:
                            print(f"{i1}{i2}{i3}{i4}{i5}{i6} ", end="")

