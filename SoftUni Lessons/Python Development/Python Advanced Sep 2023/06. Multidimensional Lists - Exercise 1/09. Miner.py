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


size = int(input())
commands = input().split(' ')
matrix = Matrix(rows=size, type_data=str, separator=' ')

coal_goal = len(matrix.find_coordinates_of_objects('c'))
collected_coal = 0
finished = False

for command in commands:
    miner = matrix.find_coordinates_of_objects('s')[0]

    next_r = matrix.delta[command][0] + miner[0]
    next_c = matrix.delta[command][1] + miner[1]

    # Check if next move is in the matrix:
    if not (matrix.coords_in_matrix(next_r, next_c)):
        continue

    # Check if the miner has reached the end:
    if matrix.data[next_r][next_c] == 'e':
        finished = True
        print(f"Game over! ({next_r}, {next_c})")
        break
    # Check if he has found coal:
    elif matrix.data[next_r][next_c] == 'c':
        collected_coal += 1
        # matrix.swap_elements(miner[0], miner[1], next_r, next_c)
        matrix.data[miner[0]][miner[1]] = "*"
        matrix.data[next_r][next_c] = 's'
        # Check if all coal was collected:
        if coal_goal == collected_coal:
            finished = True
            print(f"You collected all coal! ({next_r}, {next_c})")
    # Or else he has dug and empty hole:
    else:
        matrix.swap_elements(miner[0], miner[1], next_r, next_c)

if not finished:
    number_of_remaining_coal = coal_goal - collected_coal
    row_index, col_index = matrix.find_coordinates_of_objects('s')[0]
    print(f"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})")
