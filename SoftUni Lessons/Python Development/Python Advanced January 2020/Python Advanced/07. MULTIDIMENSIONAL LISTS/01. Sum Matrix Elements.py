def read_matrix():
    rows_count, columns_count = [int(x) for x in input().split(", ")]
    _matrix = [list(map(int, input().split(", "))) for _ in range(rows_count)]
    return _matrix


def print_matrix(matrix_to_print):
    print(matrix_to_print)


def print_sum_matrix(matrix_to_get_the_sum):
    print(sum([sum(row) for row in matrix_to_get_the_sum]))


matrix = read_matrix()
print_sum_matrix(matrix)
print_matrix(matrix)



