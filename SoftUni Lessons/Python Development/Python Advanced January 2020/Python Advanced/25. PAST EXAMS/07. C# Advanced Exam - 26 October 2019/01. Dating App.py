from collections import deque

males = [int(m) for m in input().split()]
females = deque([int(f) for f in input().split()])

matches = 0

while males and females:
    male = males[-1]
    female = females[0]
    if male % 25 == 0 or female % 25 == 0:
        if male % 25 == 0:
            males.pop()
            # if males:
            #     males.pop()
        if female % 25 == 0:
            females.popleft()
            if females:
                females.popleft()
        continue
    male = males.pop()
    if male <= 0:
        continue
    female = females.popleft()
    if female <= 0:
        males.append(male)
        continue
    if male == female:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}")
if not males:
    print(f"Males left: none")
else:
    print(f"Males left: {', '.join((str(male) for male in males[::-1]))}")
if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join([str(female) for female in females])}")
