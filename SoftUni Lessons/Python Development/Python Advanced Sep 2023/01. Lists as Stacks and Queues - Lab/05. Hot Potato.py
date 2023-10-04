from collections import deque


def solve(people, n):
    people = deque(people)
    index = 0
    while people:
        person = people.popleft()
        index += 1
        if index == n:
            index = 0
            if people:
                print(f"Removed {person}")
            else:
                print(f"Last is {person}")
        else:
            people.append(person)


solve(input().split(), int(input()))


