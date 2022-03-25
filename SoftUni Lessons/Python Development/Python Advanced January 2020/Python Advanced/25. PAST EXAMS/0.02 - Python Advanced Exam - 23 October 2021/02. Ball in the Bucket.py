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
    # IF YOU NEED JUST THE FIRST ADD [0] AFTER THE RESULT
    found_coordinates = []
    for r in range(len(matrix_to_search)):
        for c in range(len(matrix_to_search[r])):
            if matrix_to_search[r][c] == element_to_search:
                found_coordinates.append([r, c])
    return found_coordinates


def print_matrix(matrix_to_print, separator_of_elements=" "):
    output_string = ''
    for r in matrix_to_print:
        output_string += f"{separator_of_elements.join((list(map(str, r))))}\n"
    return output_string.strip()


def calculate_points_of_col(m, c):
    total = 0
    for r in range(len(m)):
        for co in range(len(m[r])):
            if co == c and m[r][co].isdigit():
                total += int(m[r][co])
    return total


score = 0
matrix = creation(rows_to_create=6, type_data_of_elements=str, separator_of_elements=" ")
prize = ''

for _ in range(3):
    x = input().split(", ")
    rol = int(x[0][1:])
    col = int((x[1].replace(")", "")))
    if check_if_element_index_is_valid(matrix, rol, col) and matrix[rol][col] == "B":
        matrix[rol][col] = "X"
        score += calculate_points_of_col(matrix, col)

if 100 <= score <= 199:
    prize = "Football"
elif 200 <= score <= 299:
    prize = "Teddy Bear"
elif score >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {score} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
