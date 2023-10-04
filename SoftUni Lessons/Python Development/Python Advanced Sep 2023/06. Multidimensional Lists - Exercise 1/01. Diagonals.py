class Matrix:
    def __init__(self):
        self.data = []

    def create(self, r, c, delimiter, type_symbols):
        [self.data.append([type_symbols(x) for x in input().split(f'{delimiter}')]) for _ in range(r)] if delimiter \
            else [self.data.append([type_symbols(x) for x in input()]) for _ in range(r)]

    def get_sum_matrix(self):
        return sum([sum(row) for row in self.data])

    def flatten(self):
        return [element for sublist in self.data for element in sublist]

    def find_coords(self, searched):
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] == searched:
                    return [r, c]
        return False

    def diagonals(self):
        primal_diagonal = [self.data[i][i] for i in range(len(self.data))]
        secondary_diagonal = [self.data[x][len(self.data) - x - 1] for x in range(len(self.data))]
        return primal_diagonal, secondary_diagonal

    def __repr__(self):
        return str(self.data)


matrix = Matrix()
matrix.create(r=int(input()), c=None, delimiter=', ', type_symbols=int)
primal, secondary = matrix.diagonals()

print(f"Primary diagonal: {', '.join([str(x) for x in primal])}. Sum: {sum(primal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
