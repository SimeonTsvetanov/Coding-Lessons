width = int(input())
length = int(input())
height = int(input())

total = width * length * height

command = None

while not(total < 0):
    command = input()
    if command == "Done":
        break
    total -= int(command)
    if total < 0:
        print(f"No more free space! You need {abs(total)} Cubic meters more.")
        break

if command == "Done":
    print(f"{total} Cubic meters left.")
