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
        return output_string.strip()


def validate_command(command_to_validate, matrix_to_check):
    valid = True
    if len(command_to_validate) == 5 and command_to_validate[0] == "swap":
        command_to_validate.remove("swap")
        row_one, col_one, row_two, col_two = [int(num) for num in command_to_validate]
        if (0 <= row_one < len(matrix_to_check)) and \
                (0 <= row_two < len(matrix_to_check)) and \
                (0 <= col_one < len(matrix_to_check[0])) and \
                (0 <= col_two < len(matrix_to_check[0])):
            return [row_one, col_one, row_two, col_two]
        else:
            valid = False
    else:
        valid = False
    return valid


rows, cols = list(map(int, input().split()))
matrix = Matrix(rows=rows, type_data=str, separator=" ")
while True:
    command = input().split()
    if command[0] == "END":
        break
    cords = validate_command(command, matrix.data)
    if cords:
        matrix.swap_elements(cords[0], cords[1], cords[2], cords[3])
        print(matrix)
    else:
        print("Invalid input!")
