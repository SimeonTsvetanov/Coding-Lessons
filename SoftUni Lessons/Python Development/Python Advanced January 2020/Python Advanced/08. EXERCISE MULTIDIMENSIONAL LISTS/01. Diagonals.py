class Matrix:
    def __init__(self, rows: int, type_data: type, separator=None):
        self.rows = rows
        self.type_data = type_data
        self.separator = separator
        self.data = Matrix.creation(self)

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
            return [[self.type_data(sym) for sym in input().split(self.separator)] for row in range(self.rows)]
        else:
            return [[self.type_data(sym) for sym in input()] for row in range(self.rows)]

    def find_coordinates_of_objects_in_2d_matrix(self, element_to_search):
        """
        list :param matrix: the 2d Matrix to search in
        any :param element_to_search: the element we will be searching for
        list of tuples :return: It will return a list of tuples(the coordinates) of all found objects
        """
        matrix = self.data
        found_coordinates = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == element_to_search:
                    found_coordinates.append((row, col))
        return found_coordinates


rows = int(input())
a = Matrix(rows=rows, type_data=int, separator=" ")
print(abs(sum(a.primary_diagonal) - sum(a.secondary_diagonal)))



