levels = int(input())
rooms = int(input())

what_type = None

for i in range(levels, 0, -1):
    for j in range(0, rooms):
        if i == levels:
            what_type = "L"
        elif i % 2 == 0:
            what_type = "O"
        elif i % 2 != 0:
            what_type = "A"
        print(f"{what_type}{i}{j} ", end="")
    print()





