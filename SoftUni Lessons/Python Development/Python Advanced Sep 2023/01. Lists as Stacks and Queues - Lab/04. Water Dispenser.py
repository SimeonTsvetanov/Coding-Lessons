water = int(input())
names = []

while True:
    name = input()
    if name == "Start":
        break
    names.append(name)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{water} liters left")
        break
    elif len(command) == 1:
        liters = int(command[0])
        name = names[0]
        names.pop(0)
        if water - liters >= 0:
            print(f"{name} got water")
            water -= liters
        else:
            print(f"{name} must wait")
    else:
        liters = int(command[1])
        water += liters
