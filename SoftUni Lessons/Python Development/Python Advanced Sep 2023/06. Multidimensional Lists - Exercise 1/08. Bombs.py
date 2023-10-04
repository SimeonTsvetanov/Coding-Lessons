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

    def coords_in_matrix(self, x, y):
        return (0 <= x < len(self.data)) and (0 <= y < len(self.data[0]))

    def swap_elements(self, x1: int, y1: int, x2: int, y2: int):
        self.data[x1][y1], self.data[x2][y2] = self.data[x2][y2], self.data[x1][y1]

    def __repr__(self):
        output_string = ''
        if self.separator:
            for r in self.data:
                output_string += f"{self.separator.join((list(map(str, r))))}\n"
        else:
            for r in self.data:
                output_string += f"{r}\n"
        return output_string.strip()


matrix = Matrix(rows=int(input()), type_data=int, separator=' ')
bombs = [[int(a) for a in x.split(',')] for x in input().split(' ')]

for bomb in bombs:
    r, c = bomb

    # check if coords of the bomb are in the matrix:
    if not matrix.coords_in_matrix(r, c):
        continue

    bomb_power = matrix.data[r][c]

    # Check if the bomb is still active:
    if matrix.data[r][c] <= 0:
        continue

    for el in matrix.delta.values():
        target_r, target_c = el[0] + r, el[1] + c

        # Check if the target isn't civilian.
        if not matrix.coords_in_matrix(target_r, target_c):
            continue

        # If there is still life in the target... take it!
        if matrix.data[target_r][target_c] > 0:
            matrix.data[target_r][target_c] -= bomb_power

    # Remove the bomb value:
    matrix.data[r][c] = 0

total = 0
alive = 0

for r in range(len(matrix.data)):
    for c in range(len(matrix.data[r])):
        if matrix.data[r][c] > 0:
            total += matrix.data[r][c]
            alive += 1

print(f"Alive cells: {alive}")
print(f"Sum: {total}")
print(matrix)

