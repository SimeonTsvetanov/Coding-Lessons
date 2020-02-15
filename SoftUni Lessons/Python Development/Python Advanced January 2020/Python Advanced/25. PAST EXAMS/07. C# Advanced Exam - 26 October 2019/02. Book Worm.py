text = input()

matrix = []
player = []

moves = {  # This are the Delta changes for the moves:
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row in range(int(input())):  # Build the matrix + get the position of the player
    line = [x for x in input()]
    matrix.append(line)
    if "P" in line:
        player = [row, line.index("P")]

while True:
    command = input()
    if command == "end":
        break
    next_row, next_col = [player[0] + moves[command][0], player[1] + moves[command][1]]  # Get the future move coords.

    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):  # So the move is valid.
        if matrix[next_row][next_col] != "-":  # If the cell is letter we will add it to the text
            text += matrix[next_row][next_col]

        matrix[player[0]][player[1]] = "-"  # Change the old players cell to empty "-"
        matrix[next_row][next_col] = "P"  # Mark the new position of the player
        player = [next_row, next_col]  # Change the players coords.

    else:  # If the move is invalid we will remove the last letter of the text, if it still exists.
        if text:
            text = text[:-1]

print(text)
[print(''.join(row)) for row in matrix]  # Print the matrix


