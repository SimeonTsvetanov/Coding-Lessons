from _collections import deque

# Work in class:

# Create a class for stack:
"""
class Stack:
    def __init__(self):
        self.internal_values = []

    def push(self, value):
        return self.internal_values.append(value)

    def pop(self):
        return self.internal_values.pop()

    def peek(self):
        return self.internal_values[-1]

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.internal_values)


s = Stack()

[s.push(x) for x in range(5)]

while not s.is_empty:
    print(s.pop())
"""

"""
The Ques has 3 methods enqueue, dequeue and peek.
"""

# This is the implementation of Queue in Python with class:
"""
class Queue:
    def __init__(self):
        self.internal_values = []
        self.start_index = 0
        self.queue_size = 0

    def enqueue(self, value):
        self.internal_values.append(value)
        self.queue_size += 1

    def dequeue(self):
        value = self.internal_values[self.start_index]
        self.start_index += 1
        self.queue_size -= 1
        return value

    def peek(self):
        return self.internal_values[self.start_index]

    def is_empty(self):
        return self.queue_size == 0


q = Queue()

[q.enqueue(x) for x in range(5)]

while not q.is_empty():
    print(q.dequeue())
"""

# append, popleft
# appendleft, pop

"""
q = deque()

q.append(1)
q.append(2)
q.append(3)

while q:
    print(q.popleft())
"""

# TODO To check leetcode.org for tasks
