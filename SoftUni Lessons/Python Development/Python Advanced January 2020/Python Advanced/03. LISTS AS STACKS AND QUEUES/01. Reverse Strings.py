# My Initial Code:
"""
string = list(input())

stack = []

for letter in range(len(string)):
    stack.append(string.pop())

print(''.join(stack))
"""

# Code from class:


def solve(string):
    reversed_str = ""

    s = list(string)

    while s:
        reversed_str += s.pop()

    return reversed_str


print(solve(input()))


