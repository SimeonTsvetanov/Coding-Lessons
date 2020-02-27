import math
from collections import deque

the_ugly_expression = input().split()
current_nums = deque([])

check = True

for symbol in the_ugly_expression:
    if symbol.isdigit() or len(symbol) >= 2:
        current_nums.append(symbol)

    else:
        if check and (symbol == "/" or symbol == "*"):
            result = 1
            check = False
        elif check:
            result = 0
            check = False

        while len(current_nums) >= 2:
            num = current_nums.popleft()
            next_num = current_nums.popleft()
            if symbol == "/":
                total = math.floor(eval(f"{num} {symbol} {next_num}"))
            else:
                total = eval(f"{num} {symbol} {next_num}")
            current_nums.appendleft(total)


print(current_nums.pop())

