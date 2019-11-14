n1 = int(input())
n2 = int(input())
n3 = int(input())

for num1 in range(1, n1 + 1):
    for num2 in range(1, n2 + 1):
        for num3 in range(1, n3 + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if 2 <= num2 <= 7:
                    if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                        print(f"{num1} {num2} {num3}")




