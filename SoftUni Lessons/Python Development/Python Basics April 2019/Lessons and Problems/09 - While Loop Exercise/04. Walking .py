total_steps = 0

while True:
    command = input()
    if command == "Going home":
        steps = int(input())
        total_steps += steps
        break
    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        break

if total_steps >= 10000:
    print("Goal reached! Good job!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")
