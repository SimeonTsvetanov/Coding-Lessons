def read_matrix():
    rows_count, columns_count = [int(x) for x in input().split(", ")]
    _matrix = [list(map(int, input().split(" "))) for _ in range(rows_count)]
    return _matrix


def get_column_sums(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    column_sums = [0] * columns_count
    for row in range(rows_count):
        for column in range(columns_count):
            column_sums[column] += matrix[row][column]
    return column_sums


[print(column_sum) for column_sum in get_column_sums(read_matrix())]
