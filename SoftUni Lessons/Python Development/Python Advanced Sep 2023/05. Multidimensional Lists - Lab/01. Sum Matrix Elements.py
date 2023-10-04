class Matrix:
    def __init__(self):
        self.data = []

    def create(self, r, c, delimiter, type_symbols):
        [self.data.append([type_symbols(x) for x in input().split(f'{delimiter}')]) for _ in range(r)]

    def get_sum_matrix(self):
        return sum([sum(row) for row in self.data])

    def __repr__(self):
        return str(self.data)


matrix = Matrix()
rows, cols = [int(x) for x in input().split(', ')]
matrix.create(rows, cols, ',', int)
print(matrix.get_sum_matrix())
print(matrix)
