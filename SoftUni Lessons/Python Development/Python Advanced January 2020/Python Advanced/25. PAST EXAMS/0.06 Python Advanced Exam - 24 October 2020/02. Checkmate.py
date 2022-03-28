def creation(rows_to_create: int, type_data_of_elements: type, separator_of_elements=""):
    return [[type_data_of_elements(sym) for sym in input().split(separator_of_elements)] for _ in range(rows_to_create)]


def find_coordinates_of_objects(matrix_to_search, element_to_search):
    # It will return a list of lists(the coordinates) of all found objects
    # IF YOU NEED JUST THE FIRST ADD [0] AFTER THE RESULT
    found_coordinates = []
    for r in range(len(matrix_to_search)):
        for c in range(len(matrix_to_search[r])):
            if matrix_to_search[r][c] == element_to_search:
                found_coordinates.append([r, c])
    return found_coordinates


def next_position(matrix_to_check, direction, current_row, current_col, check_if_valid=False, traverse=False):
    # If You Use the TRAVERSE it will work only with up, down, left and right for now!
    delta = {
        "up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, + 1],
        'up_left': [-1, -1], "up_right": [-1, +1], "down_left": [+1, -1], "down_right": [+1, +1]
        }[direction]
    next_row, next_col = [current_row + delta[0], current_col + delta[1]]
    if check_if_valid:
        if not check_if_element_index_is_valid(matrix_to_check, next_row, next_col):
            if traverse:
                delta = {
                    "up": [len(matrix_to_check) - 1, 0],
                    "down": [-(len(matrix_to_check) - 1), 0],
                    "left": [0, len(matrix_to_check[current_row]) - 1],
                    "right": [0, -(len(matrix_to_check[current_row]) - 1)]}[direction]
                next_row, next_col = [current_row + delta[0], current_col + delta[1]]
                return [next_row, next_col]
            else:
                return False
    return [next_row, next_col]


def check_if_element_index_is_valid(matrix_to_check, row_at, col_at):
    if (0 <= row_at < len(matrix_to_check)) and (0 <= col_at < len(matrix_to_check[0])):
        return True
    else:
        return False


chess = creation(rows_to_create=8, type_data_of_elements=str, separator_of_elements=" ")
queens = find_coordinates_of_objects(matrix_to_search=chess, element_to_search="Q")
angry_queens = []

for queen in queens:
    can_capture = False
    for position in ["up", "down", "left", "right", 'up_left', "up_right", "down_left", "down_right"]:
        current = queen
        if can_capture:
            break
        while True:
            next_move = next_position(chess, position, current[0], current[1], check_if_valid=True)
            if not next_move:
                break
            if chess[next_move[0]][next_move[1]] == "K":
                angry_queens.append(queen)
                can_capture = True
                break
            if chess[next_move[0]][next_move[1]] == "Q":
                break
            current = next_move

if angry_queens:
    [print(q) for q in angry_queens]
else:
    print("The king is safe!")
