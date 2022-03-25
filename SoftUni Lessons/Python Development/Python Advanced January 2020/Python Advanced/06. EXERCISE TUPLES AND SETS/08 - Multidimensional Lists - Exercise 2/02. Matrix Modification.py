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

    def next_position(self, direction, current_row, current_col, check_if_valid=False):
        delta = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, + 1]}[direction]
        next_row, next_col = [current_row + delta[0], current_col + delta[1]]
        if check_if_valid:
            if not self.check_if_element_index_is_valid(r=next_row, c=next_col):
                return False
        return [next_row, next_col]

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

    def check_if_element_index_is_valid(self, r, c):
        if (0 <= r < len(self.data)) and (0 <= c < len(self.data[0])):
            return True
        else:
            return False

    def __repr__(self):
        output_string = ''
        for r in self.data:
            output_string += f"{' '.join((list(map(str, r))))}\n"
        return output_string


size = int(input())
matrix = Matrix(rows=size, type_data=int, separator=" ")

while True:
    command = input().split()
    if command[0] == "END":
        print(matrix)
        break
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if command[0] == "Add":
        if matrix.check_if_element_index_is_valid(r=row, c=col):
            matrix.data[row][col] += value
        else:
            print(f"Invalid coordinates")
    elif command[0] == "Subtract":
        if matrix.check_if_element_index_is_valid(r=row, c=col):
            matrix.data[row][col] -= value
        else:
            print(f"Invalid coordinates")
