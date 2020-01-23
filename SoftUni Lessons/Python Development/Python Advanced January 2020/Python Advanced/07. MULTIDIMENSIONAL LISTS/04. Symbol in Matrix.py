def read_matrix():
    rows_count = int(input())
    _matrix = [list(input()) for _ in range(rows_count)]
    _symbol = input()
    return _matrix, _symbol


def get_position(_matrix, _symbol):
    found_row = 0
    found_col = 0
    is_found = False
    for row in range(len(_matrix)):
        if is_found:
            break
        for col in range(len(_matrix[0])):
            if _matrix[row][col] == _symbol:
                found_row = row
                found_col = col
                is_found = True
                break
    if not is_found:
        print(f"{_symbol} does not occur in the matrix")
    else:
        print(f"({found_row}, {found_col})")


matrix, symbol = read_matrix()
get_position(matrix, symbol)
