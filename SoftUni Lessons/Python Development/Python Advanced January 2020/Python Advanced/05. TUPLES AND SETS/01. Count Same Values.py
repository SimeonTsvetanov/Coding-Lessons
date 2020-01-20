# This is my initial solution:

"""
numbers = {}

nums = [float(x) for x in input().split()]

for num in nums:
    if num not in numbers:
        numbers[num] = 1
    else:
        numbers[num] += 1

for number, times in numbers.items():
    print(f"{number} - {times} times")
"""

# And this is the solution form class:


def solve(values):
    occurances = {}
    for value in values:
        if value not in occurances:
            occurances[value] = 0
        occurances[value] += 1
    for number, count in occurances.items():
        print(f"{number} - {count} times")


values_strings = input().split(' ')
values = [float(x) for x in values_strings]
solve(values)
