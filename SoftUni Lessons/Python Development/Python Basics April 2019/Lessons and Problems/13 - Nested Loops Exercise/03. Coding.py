n = input()

for num in reversed(n):
    num = int(num)
    for i in range(num):
        if num != 0:
            s = chr(num + 33)
            print(s, end="")
    if num == 0:
        print("ZERO")
    else:
        print()