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

    @staticmethod
    def next_position(direction, current_row, current_col):
        delta = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, + 1]}[direction]
        return [current_row + delta[0], current_col + delta[1]]

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
            output_string += f"{''.join((list(map(str, r))))}\n"
        return output_string.strip()


matrix_rows, matrix_cols = list(map(int, (input().split(" "))))
matrix = Matrix(rows=matrix_rows, type_data=str, separator="")
player_row, player_col = matrix.find_coordinates_of_objects("P")[0]
bunny_row, bunny_col = matrix.find_coordinates_of_objects("B")[0]
commands = [command for command in input()]
directions = {"U": "up", "D": "down", "L": "left", "R": "right"}
escaped_or_died = False
message = ''
for command in commands:
    player_row, player_col = matrix.find_coordinates_of_objects("P")[0]
    direction = directions[command]
    player_next_row, player_next_col = matrix.next_position(direction=direction, current_row=player_row, current_col=player_col)
    if not matrix.check_if_element_index_is_valid(r=player_next_row, c=player_next_col):
        # Player has WON
        matrix.data[player_row][player_col] = "."
        message = f"won: {player_row} {player_col}"
        escaped_or_died = True
    elif matrix.data[player_next_row][player_next_col] == ".":
        # Walk quite not to awake any bunnies!
        matrix.data[player_row][player_col] = "."
        matrix.data[player_next_row][player_next_col] = "P"
    elif matrix.data[player_next_row][player_next_col] == "B":
        # Player is DEAD
        matrix.data[player_row][player_col] = "."
        escaped_or_died = True
        message = f"dead: {player_next_row} {player_next_col}"
    # We need condoms
    for bunny_row, bunny_col in matrix.find_coordinates_of_objects("B"):
        for bunny_direction in ["up", "down", "left", "right"]:
            next_b_row, next_b_col = matrix.next_position(bunny_direction, bunny_row, bunny_col)
            if matrix.check_if_element_index_is_valid(r=next_b_row, c=next_b_col):
                if matrix.data[next_b_row][next_b_col] == ".":
                    matrix.data[next_b_row][next_b_col] = "B"
                elif matrix.data[next_b_row][next_b_col] == "P":
                    # We are sorry
                    matrix.data[next_b_row][next_b_col] = "B"
                    message = f"dead: {next_b_row} {next_b_col}"
                    escaped_or_died = True
    if escaped_or_died:
        print(matrix)
        print(message)
        break
