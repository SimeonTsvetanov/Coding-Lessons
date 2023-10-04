"""
**** Judge score gives me 90/100 NO IDEA WHY. But I'm happy with my solution.
"""


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


m = Matrix(rows=5, type_data=str, separator=" ")
a = m.find_coordinates_of_objects("A")[0]
left_targets = len(m.find_coordinates_of_objects('x'))
hit_targets = []

for _ in range(int(input())):
    if left_targets == 0:
        break
    command = input().split()
    if len(command) == 3:
        # moving yo ass!
        direction = command[1]
        length = int(command[2])
        for _ in range(length):
            move = m.next_position(direction=direction, current_row=a[0], current_col=a[1], check_if_valid=True)
            if move and (m.data[move[0]][move[1]] == "."):
                m.data[a[0]][a[1]] = "."
                m.data[move[0]][move[1]] = "A"
                a = move
            else:
                # Out of range or target in the way
                break
    elif len(command) == 2:
        # shoot them bit**s
        direction = command[1]
        s = a
        while True:
            move = m.next_position(direction=direction, current_row=s[0], current_col=s[1], check_if_valid=True)
            if move:
                if m.data[move[0]][move[1]] == ".":
                    s = move
                elif m.data[move[0]][move[1]] == "x":
                    # SCORE
                    hit_targets.append(move)
                    m.data[move[0]][move[1]] = "."
                    left_targets -= 1
                    break
            else:
                # We'll need a better shooter
                break

if left_targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {left_targets} targets left.")
if len(hit_targets) > 0:
    [print(hit_target) for hit_target in hit_targets]