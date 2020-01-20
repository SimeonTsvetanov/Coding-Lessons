# This is my initial solution:
"""
from collections import deque


def solve():
    n, s, x = (int(element) for element in input().split())

    queue = deque()
    [queue.append(int(num)) for num in input().split()]

    [queue.popleft() for _ in range(s)]
    if x in queue:
        print("True")
    elif len(queue) >= 1:
        print(min(queue))
    else:
        print(0)


if __name__ == '__main__':
    solve()
"""

# And this is the solution from work in class:
from collections import deque

numbers = [int(x) for x in input().split(" ")]

to_enqueue, to_dequeue, searched_number = numbers

queue = deque([int(x) for x in input().split(" ")])

for _ in range(to_dequeue):
    queue.popleft()

if searched_number in queue:
    print("True")
else:
    if queue:
        print(min(queue))
    else:
        print(0)
