def creation(rows_to_create: int, type_data_of_elements: type, separator_of_elements=None):
    if separator_of_elements:
        return [[type_data_of_elements(sym) for sym in input().split(separator_of_elements)] for _ in range(rows_to_create)]
    else:
        return [[type_data_of_elements(sym) for sym in input()] for _ in range(rows_to_create)]


def next_position(matrix_to_check, direction, current_row, current_col, check_if_valid=False):
    delta = {
        "up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, + 1],
        'up_left': [-1, -1], "up_right": [-1, +1], "down_left": [+1, -1], "down_right": [+1, +1]
        }[direction]
    next_row, next_col = [current_row + delta[0], current_col + delta[1]]
    if check_if_valid:
        if not check_if_element_index_is_valid(matrix_to_check, next_row, next_col):
            return False
    return [next_row, next_col]


def check_if_element_index_is_valid(matrix_to_check, row_at, col_at):
    if (0 <= row_at < len(matrix_to_check)) and (0 <= col_at < len(matrix_to_check[0])):
        return True
    else:
        return False


def find_coordinates_of_objects(matrix_to_search, element_to_search):
    # It will return a list of lists(the coordinates) of all found objects
    found_coordinates = []
    for r in range(len(matrix_to_search)):
        for c in range(len(matrix_to_search[r])):
            if matrix_to_search[r][c] == element_to_search:
                found_coordinates.append([r, c])
    return found_coordinates


chest = creation(rows_to_create=8, type_data_of_elements=str, separator_of_elements=" ")
# print(print_matrix(chest, separator_of_elements=" "))
col = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
row = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}

w = find_coordinates_of_objects(chest, "w")[0]
b = find_coordinates_of_objects(chest, "b")[0]


while True:
    for direction in ["up_left", "up_right"]:
        move = next_position(chest, direction, w[0], w[1], check_if_valid=True)
        if move and (chest[move[0]][move[1]] == 'b'):
            chest[w[0]][w[1]] = '-'
            w = move
            chest[move[0]][move[1]] = 'w'
            print(f"Game over! White win, capture on {col[w[1]]}{row[w[0]]}.")
            quit()

    move = next_position(chest, 'up', w[0], w[1], check_if_valid=True)
    if move and move[0] != 0:
        chest[w[0]][w[1]] = '-'
        w = move
        chest[move[0]][move[1]] = 'w'
    else:
        w = move
        print(f"Game over! White pawn is promoted to a queen at {col[w[1]]}{row[w[0]]}.")
        quit()

    for direction in ["down_left", "down_right"]:
        move = next_position(chest, direction, b[0], b[1], check_if_valid=True)
        if move and (chest[move[0]][move[1]] == 'w'):
            chest[b[0]][b[1]] = '-'
            b = move
            chest[move[0]][move[1]] = 'b'
            print(f"Game over! Black win, capture on {col[b[1]]}{row[b[0]]}.")
            quit()

    move = next_position(chest, 'down', b[0], b[1], check_if_valid=True)
    if move and move[0] != 7:
        chest[b[0]][b[1]] = '-'
        b = move
        chest[move[0]][move[1]] = 'b'
    else:
        b = move
        print(f"Game over! Black pawn is promoted to a queen at {col[b[1]]}{row[b[0]]}.")
        quit()
