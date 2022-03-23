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
        """
        integer :param rows: the rows count of the matrix
        type :param type_data: the type of elements in the matrix (int, str, float, others)
        string :param separator: the separator between the elements. It will be space if none is given.

        list :return: 2d matrix filled with the input data
        """
        if self.separator:
            return [[self.type_data(sym) for sym in input().split(self.separator)] for _ in range(self.rows)]
        else:
            return [[self.type_data(sym) for sym in input()] for _ in range(self.rows)]

    def find_coordinates_of_objects_in_2d_matrix(self, element_to_search):
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


row, col = list(map(int, input().split()))
matrix = Matrix(rows=row, type_data=str, separator=" ")
total = 0
for row in range(len(matrix.data)):
    for col in range(len(matrix.data[row])):
        if row < len(matrix.data) - 1 and col != len(matrix.data[row]) - 1:
            a, b, c, d = matrix.data[row][col], matrix.data[row][col + 1], \
                         matrix.data[row + 1][col], matrix.data[row + 1][col + 1]
            if a == b == c == d:
                total += 1

print(total)
