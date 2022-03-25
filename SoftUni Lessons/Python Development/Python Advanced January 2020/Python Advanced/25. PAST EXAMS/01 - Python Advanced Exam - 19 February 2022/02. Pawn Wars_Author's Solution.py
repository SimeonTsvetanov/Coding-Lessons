def check_if_can_capture(coordinates_attacker, coordinates_defender):
    row_a = coordinates_attacker[0]
    col_a = coordinates_attacker[1]
    row_d = coordinates_defender[0]
    col_d = coordinates_defender[1]
    if row_a - 1 >= 0 and col_a - 1 >= 0:
        if row_a - 1 == row_d and col_a - 1 == col_d:
            return [row_a - 1, col_a - 1]
    if row_a - 1 >= 0 and col_a + 1 < 8:
        if row_a - 1 == row_d and col_a + 1 == col_d:
            return [row_a - 1, col_a + 1]
    if row_a + 1 < 8 and col - 1 >= 0:
        if row_a + 1 == row_d and col_a - 1 == col_d:
            return [row_a + 1, col_a - 1]
    if row_a + 1 < 8 and col + 1 < 8:
        if row_a + 1 == row_d and col_a + 1 == col_d:
            return [row_a + 1, col_a + 1]


matrix = []
for _ in range(8):
    matrix.append(input().split())

white_pawn_coordinates = []
black_pawn_coordinates = []

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_pawn_coordinates = [row, col]
        if matrix[row][col] == "b":
            black_pawn_coordinates = [row, col]

for _ in range(8):
    capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn_coordinates[0] -= 1

    if white_pawn_coordinates[0] == 0:
        position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn_coordinates[0] += 1

    if black_pawn_coordinates[0] == 7:
        position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break
