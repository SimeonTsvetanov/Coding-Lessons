# This is my initial solution:
"""
def solve():
    stack = []
    for _ in range(int(input())):
        query = [int(element) for element in input().split()]
        if query[0] == 1:
            stack.append(query[1])
        elif query[0] == 2:
            if stack:
                stack.pop()
        elif query[0] == 3:
            if stack:
                print(max(stack))
        elif query[0] == 4:
            if stack:
                print(min(stack))
    print(", ".join([str(element) for element in stack][::-1]))


if __name__ == '__main__':
    solve()
"""

# And this is the solution from work in class:
n = int(input())
stack = []

for _ in range(n):
    numbers = [int(x) for x in input().split()]
    if numbers[0] == 1:
        stack.append(numbers[1])
    if stack:
        if numbers[0] == 2:
            stack.pop()
        elif numbers[0] == 3:
            print(max(stack))
        elif numbers[0] == 4:
            print(min(stack))

print(', '.join([str(x) for x in reversed(stack)]))
