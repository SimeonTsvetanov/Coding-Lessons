def creation(rows_to_create: int, type_data_of_elements: type, separator_of_elements=None):
    if separator_of_elements:
        return [[type_data_of_elements(sym) for sym in input().split(separator_of_elements)] for _ in range(rows_to_create)]
    else:
        return [[type_data_of_elements(sym) for sym in input()] for _ in range(rows_to_create)]


def next_position(matrix_to_check, direction, current_row, current_col, check_if_valid=False):
    delta = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, + 1]}[direction]
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


def print_matrix(matrix_to_print, separator_of_elements):
    output_string = ''
    for r in matrix_to_print:
        output_string += f"{separator_of_elements.join((list(map(str, r))))}\n"
    return output_string.strip()


presents = int(input())
size = int(input())
matrix = creation(rows_to_create=size, type_data_of_elements=str, separator_of_elements=" ")
# print(print_matrix(matrix, separator_of_elements=" "))
santa = find_coordinates_of_objects(matrix, "S")[0]
good_kids_count = len(find_coordinates_of_objects(matrix, "V"))
given_presents_to_nice_kids = 0

while True:
    if presents == 0:
        break
    direction = input()
    if direction == "Christmas morning":
        break
    next_house = next_position(matrix, direction, santa[0], santa[1], check_if_valid=True)
    if not next_house:
        continue
    if matrix[next_house[0]][next_house[1]] == "V":
        # nice kid house
        presents -= 1
        given_presents_to_nice_kids += 1
        matrix[santa[0]][santa[1]] = "-"
        matrix[next_house[0]][next_house[1]] = "S"
        santa = next_house
        if presents == 0:
            break
    elif (matrix[next_house[0]][next_house[1]] == "X") or (matrix[next_house[0]][next_house[1]] == "-"):
        # bad kid house or empty space
        matrix[santa[0]][santa[1]] = "-"
        matrix[next_house[0]][next_house[1]] = "S"
        santa = next_house
    elif matrix[next_house[0]][next_house[1]] == "C":
        # cookie TIME
        matrix[santa[0]][santa[1]] = "-"
        matrix[next_house[0]][next_house[1]] = "S"
        santa = next_house
        for move in ['left', 'right', 'up', 'down']:
            h = next_position(matrix, move, santa[0], santa[1])
            if matrix[h[0]][h[1]] in ["V", "X"]:
                if matrix[h[0]][h[1]] == "V":
                    given_presents_to_nice_kids += 1
                matrix[h[0]][h[1]] = '-'
                presents -= 1
                if presents == 0:
                    break

if (presents == 0) and (good_kids_count != given_presents_to_nice_kids):
    print(f"Santa ran out of presents!")
print(print_matrix(matrix, " "))
if good_kids_count == given_presents_to_nice_kids:
    print(f"Good job, Santa! {good_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count - given_presents_to_nice_kids} nice kid/s.")
