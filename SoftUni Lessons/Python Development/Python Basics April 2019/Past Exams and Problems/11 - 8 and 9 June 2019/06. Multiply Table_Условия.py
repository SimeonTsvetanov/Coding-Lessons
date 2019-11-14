num = int(input())

x1 = int(str(num)[0])
x2 = int(str(num)[1])
x3 = int(str(num)[2])

for num1 in range(1, x3 + 1):
    for num2 in range(1, x2 + 1):
        for num3 in range(1, x1 + 1):
            print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3};")







