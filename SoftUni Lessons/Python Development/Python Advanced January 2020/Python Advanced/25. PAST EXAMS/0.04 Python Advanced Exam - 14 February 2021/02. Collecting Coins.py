def creation(rows_to_create: int, type_data_of_elements: type, separator_of_elements=None):
    if separator_of_elements:
        return [[type_data_of_elements(sym) for sym in input().split(separator_of_elements)] for _ in range(rows_to_create)]
    else:
        return [[type_data_of_elements(sym) for sym in input()] for _ in range(rows_to_create)]


def print_matrix(matrix_to_print, separator_of_elements=" "):
    output_string = ''
    for r in matrix_to_print:
        output_string += f"{separator_of_elements.join((list(map(str, r))))}\n"
    return output_string.strip()


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


size = int(input())

matrix = creation(rows_to_create=size, type_data_of_elements=str, separator_of_elements=" ")
player = find_coordinates_of_objects(matrix_to_search=matrix, element_to_search="P")[0]
coins = 0
path = []

while True:
    path.append(player)
    next_move = next_position(matrix, input(), player[0], player[1], check_if_valid=True, traverse=True)
    if matrix[next_move[0]][next_move[1]] == "X":
        # STOP THE GAME
        coins = int(coins / 2)
        print(f"Game over! You've collected {coins} coins.")
        path.append(next_move)
        break
    elif matrix[next_move[0]][next_move[1]] == "-":
        matrix[next_move[0]][next_move[1]] = "P"
        matrix[player[0]][player[1]] = "-"
        player = next_move
    elif matrix[next_move[0]][next_move[1]].isdigit():
        coins += int(matrix[next_move[0]][next_move[1]])
        matrix[next_move[0]][next_move[1]] = "P"
        matrix[player[0]][player[1]] = "-"
        player = next_move
        if coins >= 100:
            # Got them money
            print(f"You won! You've collected {coins} coins.")
            path.append(player)
            break

print("Your path:")
[print(step) for step in path]
