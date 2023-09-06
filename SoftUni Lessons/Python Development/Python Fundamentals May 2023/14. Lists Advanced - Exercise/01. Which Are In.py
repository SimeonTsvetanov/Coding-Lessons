first = [s for s in input().split(', ')]
second = [s for s in input().split(', ')]
third = []

for i in first:
    for j in second:
        if i in j and i not in third:
            third.append(i)

print(third)
