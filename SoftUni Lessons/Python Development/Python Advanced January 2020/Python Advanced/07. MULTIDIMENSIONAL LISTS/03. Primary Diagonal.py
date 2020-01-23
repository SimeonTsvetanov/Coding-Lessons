def read_matrix():
    rows_count = int(input())
    _matrix = [list(map(int, input().split(" "))) for _ in range(rows_count)]
    return _matrix


def calculate_primary_diagonal(matrix):
    the_sum = 0
    for x in range(len(matrix)):
        the_sum += matrix[x][x]
    return the_sum


def calculate_secondary_diagonal(matrix):  # This is from work in class just to calculate the secondary diagonal:
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][n - x - 1]
    return the_sum


print(calculate_primary_diagonal(read_matrix()))



