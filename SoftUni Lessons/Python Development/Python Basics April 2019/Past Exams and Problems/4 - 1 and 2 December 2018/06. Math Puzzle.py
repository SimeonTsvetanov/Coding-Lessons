key = int(input())
checker = 0

for num1 in range(1, 31):
    for num2 in range(1, 31):
        for num3 in range(1, 31):
            if num1 < num2 < num3:
                if num1 + num2 + num3 == key:
                    print(f"{num1} + {num2} + {num3} = {key}")
                    checker += 1
            if num1 > num2 > num3:
                if num1 * num2 * num3 == key:
                    print(f"{num1} * {num2} * {num3} = {key}")
                    checker += 1

if checker == 0:
    print("No!")



