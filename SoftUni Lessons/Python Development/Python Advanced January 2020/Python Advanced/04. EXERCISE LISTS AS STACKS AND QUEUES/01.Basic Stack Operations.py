# This is my solution
"""
def solve():
    n, s, x = (int(element) for element in input().split())
    stack = [int(num) for num in input().split()]
    [stack.pop() for i in range(s)]
    if x in stack:
        print("True")
    elif len(stack) >= 1:
        print(min(stack))
    else:
        print(0)
    

if __name__ == '__main__':
    solve()
"""

# And this is the solution from work in class:
numbers = [int(x) for x in input().split()]
to_push, to_pop, searched_number = numbers

elements = [int(x) for x in input().split()]

[elements.pop() for _ in range(to_pop)]

if searched_number in elements:
    print("True")
else:
    if elements:
        print(min(elements))
    else:
        print(0)


