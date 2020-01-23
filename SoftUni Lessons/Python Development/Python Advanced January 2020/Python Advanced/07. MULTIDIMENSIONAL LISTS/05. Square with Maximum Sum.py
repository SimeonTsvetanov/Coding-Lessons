def read_matrix():
    rows_count, columns_count = [int(x) for x in input().split(", ")]
    _matrix = [list(map(int, input().split(", "))) for _ in range(rows_count)]
    return _matrix


def find_best_sub_matrix(best_matrix):
    rows_count = len(best_matrix)
    columns_count = len(best_matrix[0])

    _best_sum = None
    best_start = None

    for row in range(rows_count - 1):
        for col in range(columns_count - 1):
            current_sum = best_matrix[row][col] + \
                          best_matrix[row][col + 1] + \
                          best_matrix[row + 1][col] + \
                          best_matrix[row + 1][col + 1]
            if _best_sum:
                if _best_sum < current_sum:
                    _best_sum = current_sum
                    best_start = (row, col)
            else:
                _best_sum = current_sum
                best_start = (row, col)
    row, col = best_start
    _best_sub_matrix = [
        [best_matrix[row][col], best_matrix[row][col + 1]],
        [best_matrix[row + 1][col], best_matrix[row + 1][col + 1]]
    ]
    return _best_sum, _best_sub_matrix


def print_matrix(best_sum_, best_sub_matrix_):
    for row in best_sub_matrix_:
        print(' '.join([str(num) for num in row]))
    print(best_sum_)


matrix = read_matrix()
best_sum, best_sub_matrix = find_best_sub_matrix(matrix)
print_matrix(best_sum, best_sub_matrix)
