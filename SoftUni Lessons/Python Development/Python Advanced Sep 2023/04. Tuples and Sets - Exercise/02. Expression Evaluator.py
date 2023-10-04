import math
from collections import deque

# Select which solution to use by uncommenting it from the bottom.

# Solution 1 is the best looking
# Solution 2 is the simplest but worst looking :D
# Solution 3 is the one intended to be used from SU.


def solution_one():
    expression = [symbol for symbol in input().split()]
    nums = []

    for i in expression:
        if i not in ["*", "+", "-", "/"]:
            nums.append(int(i))
        else:
            while len(nums) != 1:
                # using eval() here to solve the task. Don't cry!
                result = int(eval(f"{nums[0]} {i} {nums[1]}"))
                nums.remove(nums[0])
                nums.insert(0, result)
                nums.remove(nums[1])

    print(nums[0])


def solution_two():
    def calculator(operator, n):
        def add(n):
            total = n[0]
            for i in range(1, len(n)):
                total += n[i]
            return total

        def subtract(n):
            total = n[0]
            for i in range(1, len(n)):
                total -= n[i]
            return total

        def multiply(n):
            total = n[0]
            for i in range(1, len(n)):
                total *= n[i]
            return total

        def divide(n):
            total = n[0]
            for i in range(1, len(n)):
                total /= n[i]
            return math.floor(total)

        result = 0

        if operator == "+":
            result = add(n)
        elif operator == "-":
            result = subtract(n)
        elif operator == "*":
            result = multiply(n)
        elif operator == "/":
            result = divide(n)

        return [result]

    exp = input().split(' ')
    nums = []

    for el in exp:
        if el.isdigit() or len(el) > 1:
            nums.append(int(el))
        else:
            nums = calculator(el, nums)

    print(nums[0])


def solution_three():
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


# solution_one()
# solution_two()
# solution_three()
