n = int(input())
counter = 0
for i in range(0, n + 1):
    for j in range(i + 1):
        counter += 1
        if counter <= n:
            print(f"{counter}", end=" ")
        else:
            break
    print()

