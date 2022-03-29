def creation(rows_to_create: int, type_data_of_elements: type, separator_of_elements=""):
    return [[0 for sym in range(rows_to_create)] for _ in range(rows_to_create)]


def print_matrix(matrix_to_print, separator_of_elements=" "):
    output_string = ''
    for r in matrix_to_print:
        output_string += f"{separator_of_elements.join((list(map(str, r))))}\n"
    return output_string.strip()


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

for _ in range(int(input())):
    bomb = list(map(int, input()[1:-1].split(", ")))
    if not check_if_element_index_is_valid(matrix, bomb[0], bomb[1]):
        continue
    matrix[bomb[0]][bomb[1]] = "*"
    for direction in ["up", "down", "left", "right", 'up_left', "up_right", "down_left", "down_right"]:
        next_move = next_position(matrix, direction, bomb[0], bomb[1], check_if_valid=True)
        if next_move and matrix[next_move[0]][next_move[1]] != "*":
            matrix[next_move[0]][next_move[1]] += 1

print(print_matrix(matrix_to_print=matrix, separator_of_elements=" "))
