from collections import deque

halls_maximum_capacity = int(input())

line = [x for x in input().split()]
party = deque([])
taken_guests = []

while line:
    x = line.pop()
    if x.isalpha():
        party.append(x)
        continue
    if not party:
        continue
    new_guests = int(x)
    if halls_maximum_capacity >= sum(taken_guests) + new_guests:
        taken_guests.append(new_guests)
    else:
        print(f"{party.popleft()} -> {', '.join([str(guests) for guests in taken_guests])}")
        taken_guests = []
        line.append(x)
