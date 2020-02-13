string = input()
size = int(input())

matrix = []

# Fill the matrix
for row in range(size):
    matrix.append([symbol for symbol in input()])

# Grt the Player Position
player_position = []
for row in range(len(matrix)):
    if player_position:
        break
    for col in range(len(matrix[0])):
        if matrix[row][col] == "P":
            player_position = [row, col]
            break

for _ in range(int(input())):
    command = input()

    if command == "up":
        if (player_position[0] - 1) >= 0:  # Move is Valid
            current_holder = matrix[player_position[0] - 1][player_position[1]]
            if current_holder != "-":  # So it is some letter
                string += current_holder
            matrix[player_position[0]][player_position[1]] = "-"
            matrix[player_position[0] - 1][player_position[1]] = "P"
            player_position = [player_position[0] - 1, player_position[1]]
        else:  # Move is invalid:
            if string:
                string = string[:-1]

    if command == "down":
        if (player_position[0] + 1) < len(matrix):  # Move is Valid
            current_holder = matrix[player_position[0] + 1][player_position[1]]
            if current_holder != "-":  # So it is some letter
                string += current_holder
            matrix[player_position[0]][player_position[1]] = "-"
            matrix[player_position[0] + 1][player_position[1]] = "P"
            player_position = [player_position[0] + 1, player_position[1]]
        else:  # Move is invalid:
            if string:
                string = string[:-1]

    if command == "left":
        if player_position[1] - 1 >= 0:  # Move is Valid
            current_holder = matrix[player_position[0]][player_position[1] - 1]
            if current_holder != "-":  # So it is some letter
                string += current_holder
            matrix[player_position[0]][player_position[1]] = "-"
            matrix[player_position[0]][player_position[1] - 1] = "P"
            player_position = [player_position[0], player_position[1] - 1]
        else:  # Move is invalid:
            if string:
                string = string[:-1]

    if command == "right":
        if player_position[1] + 1 < len(matrix[0]):  # Move is Valid
            current_holder = matrix[player_position[0]][player_position[1] + 1]
            if current_holder != "-":  # So it is some letter
                string += current_holder
            matrix[player_position[0]][player_position[1]] = "-"
            matrix[player_position[0]][player_position[1] + 1] = "P"
            player_position = [player_position[0], player_position[1] + 1]
        else:  # Move is invalid:
            if string:
                string = string[:-1]

print(string)
# Print the matrix
for row in matrix:
    print(''.join(row))
