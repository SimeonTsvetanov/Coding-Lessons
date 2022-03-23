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
commands = input().split(" ")

matrix = Matrix(rows=size, type_data=str, separator=" ")
delta_changes = {
    "up": [-1, 0],
    "down": [+1, 0],
    "left": [0, -1],
    "right": [0, + 1]
}
coal_count = len(matrix.find_coordinates_of_objects('c'))
flag = True

next_row, next_col = 0, 0

for command in commands:
    miner_row, miner_col = matrix.find_coordinates_of_objects('s')[0]
    next_row, next_col = delta_changes[command][0] + miner_row, delta_changes[command][1] + miner_col
    if not matrix.check_if_element_index_is_valid(next_row, next_col):
        continue
    if matrix.data[next_row][next_col] == "c":
        coal_count -= 1
        matrix.data[miner_row][miner_col] = "*"
        matrix.data[next_row][next_col] = "s"
        if coal_count == 0:
            print(f"You collected all coal! ({next_row}, {next_col})")
            flag = False
            break
    elif matrix.data[next_row][next_col] == "e":
        matrix.data[miner_row][miner_col] = "*"
        matrix.data[next_row][next_col] = "s"
        print(f"Game over! ({next_row}, {next_col})")
        flag = False
        break
    elif matrix.data[next_row][next_col] == "*":
        matrix.swap_elements(miner_row, miner_col, next_row, next_col)
    # print(matrix)

if flag:
    print(f"{coal_count} pieces of coal left. ({next_row}, {next_col})")
