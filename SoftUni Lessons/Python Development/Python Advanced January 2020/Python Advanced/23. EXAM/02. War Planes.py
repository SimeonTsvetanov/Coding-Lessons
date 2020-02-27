ugly_field = []
ugly_plane_position = []
targets_count = 0
check = False
for row in range(int(input())):
    line = input().split()
    ugly_field.append(line)
    if "p" in line:
        ugly_plane_position = [row, line.index("p")]
    if "t" in line:
        targets_count += line.count("t")

starting_targets = targets_count

for each_time in range(int(input())):

    do = input().split()
    if do[0] == "move":
        direction = do[1]
        steps = int(do[2])
        future_row = 0
        future_col = 0

        if direction == "up":
            future_row = ugly_plane_position[0] - steps
            future_col = ugly_plane_position[1]
        elif direction == "down":
            future_row = ugly_plane_position[0] + steps
            future_col = ugly_plane_position[1]
        elif direction == "left":
            future_row = ugly_plane_position[0]
            future_col = ugly_plane_position[1] - steps
        elif direction == "right":
            future_row = ugly_plane_position[0]
            future_col = ugly_plane_position[1] + steps

        if 0 <= future_row < len(ugly_field) and 0 <= future_col < len(ugly_field[future_row]):
            if ugly_field[future_row][future_col] == ".":
                ugly_field[ugly_plane_position[0]][ugly_plane_position[1]] = "."
                ugly_field[future_row][future_col] = "p"
                ugly_plane_position = [future_row, future_col]

    elif do[0] == "shoot":
        direction = do[1]
        steps = int(do[2])
        future_row = 0
        future_col = 0

        if direction == "up":
            future_row = ugly_plane_position[0] - steps
            future_col = ugly_plane_position[1]
        elif direction == "down":
            future_row = ugly_plane_position[0] + steps
            future_col = ugly_plane_position[1]
        elif direction == "left":
            future_row = ugly_plane_position[0]
            future_col = ugly_plane_position[1] - steps
        elif direction == "right":
            future_row = ugly_plane_position[0]
            future_col = ugly_plane_position[1] + steps

        if 0 <= future_row < len(ugly_field) and 0 <= future_col < len(ugly_field[future_row]):
            if ugly_field[future_row][future_col] == ".":
                ugly_field[future_row][future_col] = "x"
            elif ugly_field[future_row][future_col] == "x":
                pass
            else:
                ugly_field[future_row][future_col] = "x"
                targets_count -= 1
                check = True

    if targets_count == 0:
        break

if targets_count <= 0 and check:
    print(f"Mission accomplished! All {starting_targets} targets destroyed.")

else:
    print(f"Mission failed! {targets_count} targets left.")

for row in ugly_field:
    print(' '.join(row))
