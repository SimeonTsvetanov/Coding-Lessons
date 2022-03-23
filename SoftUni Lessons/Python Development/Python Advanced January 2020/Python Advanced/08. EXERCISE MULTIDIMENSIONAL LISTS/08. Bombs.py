class Matrix:
    def __init__(self, rows: int, type_data: type, separator=None):
        self.rows = rows
        self.type_data = type_data
        self.separator = separator
        self.data = Matrix.creation(self)

    @property
    def sum_numbers(self):
        if (self.type_data == int) or (self.type_data == float):
            return sum([sum(r) for r in self.data])
        return "Elements aren't numbers"

    @property
    def flat_matrix(self):
        return [j for sub in self.data for j in sub]

    @property
    def primary_diagonal(self):
        return [self.data[i][i] for i in range(len(self.data))]

    @property
    def secondary_diagonal(self):
        return [self.data[i][len(self.data) - i - 1] for i in range(len(self.data))]

    def creation(self):
        if self.separator:
            return [[self.type_data(sym) for sym in input().split(self.separator)] for _ in range(self.rows)]
        else:
            return [[self.type_data(sym) for sym in input()] for _ in range(self.rows)]

    def find_coordinates_of_objects(self, element_to_search):
        """
        list :param matrix: the 2d Matrix to search in
        any :param element_to_search: the element we will be searching for
        list of tuples :return: It will return a list of tuples(the coordinates) of all found objects
        """
        found_coordinates = []
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] == element_to_search:
                    found_coordinates.append((r, c))
        return found_coordinates

    def swap_elements(self, x_1: int, y_1: int, x_2: int, y_2: int):
        self.data[x_1][y_1], self.data[x_2][y_2] = self.data[x_2][y_2], self.data[x_1][y_1]

    def __repr__(self):
        output_string = ''
        for r in self.data:
            output_string += f"{' '.join((list(map(str, r))))}\n"
        return output_string


num = int(input())
matrix = Matrix(rows=num, type_data=int, separator=" ")
coordinates = [[int(n) for n in s.split(",")] for s in input().split(" ")]

for coord in coordinates:
    r, c = coord
    # print(matrix.data[r][c])
    if matrix.data[r][c] <= 0:
        continue
    for el in [[r - 1, c - 1], [r - 1, c], [r - 1, c + 1], [r, c - 1], [r, c + 1], [r + 1, c - 1], [r + 1, c], [r + 1, c + 1]]:
        if 0 <= el[0] < len(matrix.data):
            if 0 <= el[1] < len(matrix.data[0]):
                if matrix.data[el[0]][el[1]] > 0:
                    matrix.data[el[0]][el[1]] -= matrix.data[r][c]
    matrix.data[r][c] = 0

total = 0
length = 0
for r in range(len(matrix.data)):
    for c in range(len(matrix.data[r])):
        if matrix.data[r][c] > 0:
            total += matrix.data[r][c]
            length += 1

print(f"Alive cells: {length}")
print(f"Sum: {total}")
print(matrix)
