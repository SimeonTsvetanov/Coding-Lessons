matrix = []
player_one_position = []
player_two_position = []

# This are the delta changes
moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row in range(int(input())):  # Get the matrix, first and second player coordinates
    line = input()
    matrix.append([x for x in line])  # Fill the matrix
    if "f" in line:
        player_one_position = [row, line.index("f")]  # Create the initial position of player one
    if "s" in line:
        player_two_position = [row, line.index("s")]  # Create the initial position of player two


def change_position_if_out(player: list):
    """
    This Function will check if players next position will be still in the matrix.
    And if is out of the matrix it will change it to the other side instead.
    :param player: The player we want to check and/or change
    :return: the modified(or not) coordinates of the player
    """
    if 0 <= player[0] < len(matrix):
        if 0 <= player[1] < len(matrix[0]):
            return player
        else:
            if player[1] < 0:
                return [player[0], len(matrix[0]) - 1]
            else:
                return [player[0], 0]
    else:
        if player[0] < 0:
            return [len(matrix) - 1, player[1]]
        else:
            return [0, player[1]]


crash = False
while not crash:
    x = input().split()

    # First player next move + we will check if the move is possible and if not we will fix it:
    one_next_move = \
        change_position_if_out([moves[x[0]][0] + player_one_position[0], moves[x[0]][1] + player_one_position[1]])

    # Second player next move + we will check if the move is possible and if not we will fix it:
    two_next_move = \
        change_position_if_out([moves[x[1]][0] + player_two_position[0], moves[x[1]][1] + player_two_position[1]])

    # Now lets check if player ONE - next cell is free and we can step on it:
    if matrix[one_next_move[0]][one_next_move[1]] in ["*", "f"]:
        matrix[one_next_move[0]][one_next_move[1]] = "f"
        player_one_position = [one_next_move[0], one_next_move[1]]
    else:
        matrix[one_next_move[0]][one_next_move[1]] = "x"
        crash = True
        continue

    # Now lets check if player TWO - next cell is free and we can step on it:
    if matrix[two_next_move[0]][two_next_move[1]] in ["*", "s"]:
        matrix[two_next_move[0]][two_next_move[1]] = "s"
        player_two_position = [two_next_move[0], two_next_move[1]]
    else:
        matrix[two_next_move[0]][two_next_move[1]] = "x"
        crash = True

[print(''.join(line)) for line in matrix]  # Print the matrix
