from collections import deque

# read a string with N integers from the console, separated by a single space
integers = deque((input().split(' ')))
# reverse them using a stack:
new = integers.__reversed__()
# Print the reversed integers on one line, separated by a single space:
print(*list(new))
