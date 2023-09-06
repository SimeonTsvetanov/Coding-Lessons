times = [int(x) for x in input().split(' ')]
# times = [29, 13, 9, 0, 13, 0, 21, 0, 14, 82, 12]
finishIndex = int(((len(times) - 1) / 2))
leftTimes = times[0:finishIndex]
rightTimes = times[finishIndex + 1:][::-1]


def calculate(t):
    total = 0
    for current_time in t:
        if current_time != 0:
            total += current_time
        else:
            total *= 0.8
    return total


totalLeft = calculate(leftTimes)
totalRight = calculate(rightTimes)

if totalRight >= totalLeft:
    print(f"The winner is left with total time: {totalLeft:.1f}")
else:
    print(f"The winner is right with total time: {totalRight:.1f}")
