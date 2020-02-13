paris_energy = int(input())

# Get the matrix of the city
city = [[x for x in input()] for row in range(int(input()))]

# Get Paris and Helen Initial positions
paris_position = []
helen_position = []
for row in range(len(city)):
    for col in range(len(city[0])):
        if city[row][col] == "P":
            paris_position = [row, col]
        elif city[row][col] == "H":
            helen_position = [row, col]

# Setting up the directions as delta changes:
directions = {
    "up": [-1, 0],
    "down": [+1, 0],
    "left": [0, -1],
    "right": [0, +1]}

they_escaped = False
while True:
    if they_escaped or paris_energy <= 0:
        break
    command = input().split()

    direction = directions[command[0]]  # The Direction of Paris.

    city[int(command[1])][int(command[2])] = "S"  # Spawn the bad guys in the city.

    paris_energy -= 1  # Paris will aways spend 1 energy even if can't move.

    # Now lets first check if we can move Paris
    if (0 <= (paris_position[0] + direction[0]) < len(city)) and \
            (0 <= (paris_position[1] + direction[1]) < len(city[0])):

        city[paris_position[0]][paris_position[1]] = "-"  # Marking the old Paris position with empty cell.
        if paris_energy <= 0:  # We need to check if he ran out of energy:
            city[paris_position[0] + direction[0]][paris_position[1] + direction[1]] = "X"
            paris_position = [paris_position[0] + direction[0], paris_position[1] + direction[1]]
            continue

        # Now since he can move, lets check if we have s soldier there:
        if city[paris_position[0] + direction[0]][paris_position[1] + direction[1]] == "S":
            paris_energy -= 2  # If so he will loose Additional 2 health
            if paris_energy <= 0:
                city[paris_position[0] + direction[0]][paris_position[1] + direction[1]] = "X"
                paris_position = [paris_position[0] + direction[0], paris_position[1] + direction[1]]
                continue

        # Ok so lets Check if Helen is there:
        elif city[paris_position[0] + direction[0]][paris_position[1] + direction[1]] == "H":
            they_escaped = True
            city[helen_position[0]][helen_position[1]] = "-"
            continue

        # If he has not died or escaped we will change his position to the new one:
        if paris_energy > 0 and not they_escaped:
            city[paris_position[0] + direction[0]][paris_position[1] + direction[1]] = "P"
            paris_position = [paris_position[0] + direction[0], paris_position[1] + direction[1]]

if they_escaped:
    print(f"Paris has successfully abducted Helen! Energy left: {paris_energy}")
else:
    print(f"Paris died at {paris_position[0]};{paris_position[1]}.")

# Print The city
[print(''.join(row)) for row in city]
