# Judge will give only  77 / 100 (no idea why)...


class Matrix:
    delta = {
        'up_left': [-1, -1], 'up': [-1, 0], 'up_right': [-1, 1],
        'left': [0, -1], 'right': [0, 1],
        'down_left': [1, -1], 'down': [1, 0], 'down_right': [1, 1]
    }

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
        list of tuples :return: It will return a list of lists[the coordinates] of all found objects
        """
        found_coordinates = []
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] == element_to_search:
                    found_coordinates.append([r, c])
        return found_coordinates

    def coords_in_matrix(self, r, c):
        return (0 <= r < len(self.data)) and (0 <= c < len(self.data[0]))

    def next_position(self, direction, current_row, current_col, check_if_valid=False):
        next_row, next_col = [current_row + matrix.delta[direction][0], current_col + matrix.delta[direction][1]]
        if check_if_valid:
            if not self.coords_in_matrix(r=next_row, c=next_col):
                return False
        return [next_row, next_col]

    def swap_elements(self, x1: int, y1: int, x2: int, y2: int):
        self.data[x1][y1], self.data[x2][y2] = self.data[x2][y2], self.data[x1][y1]

    def __repr__(self):
        output_string = ''
        if self.separator:
            for r in self.data:
                output_string += f"{self.separator.join((list(map(str, r))))}\n"
        else:
            for r in self.data:
                output_string += f"{''.join([str(x) for x in r])}\n"
        return output_string.strip()


matrix = Matrix(rows=int(input()), type_data=str, separator=' ')
alice = matrix.find_coordinates_of_objects('A')[0]

tea = 0
while True:
    matrix.data[alice[0]][alice[1]] = '*'
    direction = matrix.delta[input()]
    next_spot = [alice[0] + direction[0], alice[1] + direction[1]]
    if (not matrix.coords_in_matrix(next_spot[0], next_spot[1])) or (matrix.data[next_spot[0]][next_spot[1]] == "R"):
        if matrix.data[next_spot[0]][next_spot[1]] == "R":
            matrix.data[next_spot[0]][next_spot[1]] = "*"
        print(f"Alice didn't make it to the tea party.")
        print(matrix)
        break
    elif matrix.data[next_spot[0]][next_spot[1]].isdigit():
        alice = next_spot
        tea += int(matrix.data[next_spot[0]][next_spot[1]])
        if tea >= 10:
            matrix.data[next_spot[0]][next_spot[1]] = "*"
            print(f"She did it! She went to the party.")
            print(matrix)
            break
    else:
        alice = next_spot
