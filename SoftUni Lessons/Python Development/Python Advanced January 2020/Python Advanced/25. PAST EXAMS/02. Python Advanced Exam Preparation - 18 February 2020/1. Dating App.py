from collections import deque

males = [int(male) for male in input().split()]
females = deque([int(female) for female in input().split()])

matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()
    if male <= 0 or female <= 0:
        if male <= 0:
            females.appendleft(female)
        if female <= 0:
            males.append(male)
    else:
        if female % 25 == 0:
            females.popleft()
            males.append(male)
        elif male % 25 == 0:
            males.pop()
            females.appendleft(female)
        else:
            if female == male:
                matches += 1
            else:
                males.append(male - 2)


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(male) for male in males[::-1]])}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join([str(female) for female in females])}")
else:
    print(f"Females left: none")
