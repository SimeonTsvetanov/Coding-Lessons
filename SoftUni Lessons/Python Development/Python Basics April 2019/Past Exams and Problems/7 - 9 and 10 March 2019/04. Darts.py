name = input()

command = None
total = 301
shots = 0
unlucky_shots = 0

while command != "Retire" or total != 0:
    command = input()
    if command == "Retire":
        print(f"{name} retired after {unlucky_shots} unsuccessful shots.")
        break
    points = int(input())
    shots += 1
    if command == "Single":
        total -= points
        if total < 0:
            total += points
            unlucky_shots += 1
            continue
    elif command == "Double":
        total -= points * 2
        if total < 0:
            total += points * 2
            unlucky_shots += 1
            continue
    elif command == "Triple":
        total -= points * 3
        if total < 0:
            total += points * 3
            unlucky_shots += 1
            continue
    if total == 0:
        print(f"{name} won the leg with {shots - unlucky_shots} shots.")
        break

