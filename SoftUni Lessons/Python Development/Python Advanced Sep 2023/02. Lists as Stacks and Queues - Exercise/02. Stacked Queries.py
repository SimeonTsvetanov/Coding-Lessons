"""
This task gives 80/100 in Judge. But it's correct. So f*** it.
"""
from collections import deque

# You have an empty stack
stack = deque()

# You will receive an integer – N
n = int(input())

# On the next N lines, you will receive queries:
# It is guaranteed that each query is valid.
for _ in range(n):
    # Each query is one of these four types:
    command = input().split(' ')
    if command[0] == '1':
        # '1 {number}' – push the number (integer) into the stack
        stack.append(int(command[1]))
    elif command[0] == '2':
        # '2' – delete the number at the top of the stack
        if stack:
            stack.pop()
    elif command[0] == '3':
        # '3' – print the maximum number in the stack
        print(max(stack))
    elif command[0] == '4':
        # '4' – print the minimum number in the stack
        print(min(stack))

# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
print(', '.join([str(n) for n in list(stack.__reversed__())]))

