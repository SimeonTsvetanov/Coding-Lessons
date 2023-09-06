s = int(input())

[print('*' * (i + 1)) for i in range(s)]
[print('*' * (i - 1)) for i in range(s, 0, -1)]
