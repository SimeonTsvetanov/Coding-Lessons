n, m = [int(num) for num in input().split()]
[print(num) for num in set(int(input()) for _ in range(n)) & set(int(input()) for _ in range(m))]
