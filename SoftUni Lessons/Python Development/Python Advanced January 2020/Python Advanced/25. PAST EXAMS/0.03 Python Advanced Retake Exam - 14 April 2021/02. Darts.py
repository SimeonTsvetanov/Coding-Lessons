def creation(rows_to_create: int, type_data_of_elements: type, separator_of_elements=None):
    if separator_of_elements:
        return [[type_data_of_elements(sym) for sym in input().split(separator_of_elements)] for _ in range(rows_to_create)]
    else:
        return [[type_data_of_elements(sym) for sym in input()] for _ in range(rows_to_create)]


def check_if_element_index_is_valid(matrix_to_check, row_at, col_at):
    if (0 <= row_at < len(matrix_to_check)) and (0 <= col_at < len(matrix_to_check[0])):
        return True
    else:
        return False


def play(player, r, c):
    global winner
    player["turns"] += 1
    if not check_if_element_index_is_valid(darts, r, c):
        return
    if darts[r][c].isdigit():
        player["score"] -= int(darts[r][c])
    elif darts[r][c] == "D":
        player["score"] -= (int(darts[r][0]) + int(darts[r][-1]) + int(darts[0][c]) + int(darts[-1][c])) * 2
    elif darts[r][c] == "T":
        player["score"] -= (int(darts[r][0]) + int(darts[r][-1]) + int(darts[0][c]) + int(darts[-1][c])) * 3
    elif darts[r][c] == "B":
        winner = player
    if player["score"] <= 0:
        winner = player
    return


name_one, name_two = input().split(", ")

player_one = {
    "name": name_one,
    "turns": 0,
    "score": 501
}
player_two = {
    "name": name_two,
    "turns": 0,
    "score": 501
}
current = player_one

winner = None
darts = creation(rows_to_create=7, type_data_of_elements=str, separator_of_elements=" ")
turn = 1

while not winner:
    shot_row, shot_col = eval(input())
    if turn % 2 != 0:
        play(player_one, int(shot_row), int(shot_col))
    else:
        play(player_two, int(shot_row), int(shot_col))

    turn += 1

print(f"{winner['name']} won the game with {winner['turns']} throws!")
