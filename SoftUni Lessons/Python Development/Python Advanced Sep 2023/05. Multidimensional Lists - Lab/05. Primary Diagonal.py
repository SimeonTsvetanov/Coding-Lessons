class Matrix:
    def __init__(self):
        self.data = []

    def create(self, r, c, delimiter, type_symbols):
        [self.data.append([type_symbols(x) for x in input().split(f'{delimiter}')]) for _ in range(r)]

    def get_sum_matrix(self):
        return sum([sum(row) for row in self.data])

    def __repr__(self):
        return str(self.data)

    def flatten(self):
        return [element for sublist in self.data for element in sublist]


matrix = Matrix()
matrix.create(r=int(input()), c=None, delimiter=' ', type_symbols=int)

result = sum([matrix.data[i][i] for i in range(len(matrix.data))])
print(result)
