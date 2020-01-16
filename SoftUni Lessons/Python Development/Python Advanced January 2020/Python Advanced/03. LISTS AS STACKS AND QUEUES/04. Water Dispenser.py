# This is the solution from work in class
from collections import deque


def solve():
    liters = int(input())
    people = deque()

    while True:
        person = input()
        if person == "Start":
            break
        people.append(person)

    while people:
        command = input()
        if command.startswith("refill"):
            liters += int(command.split()[1])
            continue
        person = people.popleft()
        person_liters = int(command)
        if liters < person_liters:
            print(f"{person} must wait")
        else:
            liters -= person_liters
            print(f"{person} got water")

    print(f"{liters} liters left")


solve()
