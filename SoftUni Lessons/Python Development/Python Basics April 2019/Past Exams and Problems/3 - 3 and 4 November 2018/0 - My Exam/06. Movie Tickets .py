a1 = int(input())
a2 = int(input())
n = int(input())

for sym_1 in range(a1, a2):
    for sym_2 in range(1, n):
        for sym_3 in range(1, int(n / 2)):
            if sym_1 % 2 != 0:
                if (sym_1 + sym_2 + sym_3) % 2 != 0:
                    print(f"{chr(sym_1)}-{sym_2}{sym_3}{sym_1}")


