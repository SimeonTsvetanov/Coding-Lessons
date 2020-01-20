# Solution from work in class:
clothes = [int(x) for x in input().split()]
rack = int(input())
rack_count = 0
total = 0

while clothes:
    current = clothes[-1]
    if rack >= total + current:
        total += clothes.pop()
    else:
        total = 0
        rack_count += 1

if total > 0:
    rack_count += 1

print(rack_count)
