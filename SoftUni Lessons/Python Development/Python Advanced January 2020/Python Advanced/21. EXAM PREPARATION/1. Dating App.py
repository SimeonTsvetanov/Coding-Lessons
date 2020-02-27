from collections import deque

males = [int(m) for m in input().split()]
females = deque([int(f) for f in input().split()])

matches = 0

while males and females:
    current_female = females[0]
    current_male = males[-1]
    if current_female <= 0:
        females.popleft()
        continue
    elif current_male <= 0:
        males.pop()
    elif current_female == current_male:
        females.popleft()
        males.pop()
        matches += 1
    elif current_female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    elif current_male % 25 == 0:
        males.pop()
        if males:
            males.pop()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in males[::-1]])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print(f"Females left: none")
