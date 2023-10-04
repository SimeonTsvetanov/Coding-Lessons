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


presents = int(input())  # for the number of presents Santa has
size = int(input())  # an integer n for the size of the neighborhood with a square shape

# On the following lines, you will receive the matrix, which represents the neighborhood:
matrix = Matrix(rows=size, type_data=str, separator=' ')

# Santa will be in a random cell, marked with the letter "S"
santa = matrix.find_coordinates_of_objects("S")[0]

given_presents = 0


"""
Each cell stands for a house where children may live. 
 - X - If the cell has an "X" on it, that means there lives a naughty kid. 
 - V - Otherwise, if a nice kid lives there, the cell is marked with "V". 
 - C - There can also be cells marked with "C" for cookies. 
All of the empty positions will be marked with "-".
"""

while True:
    """
    Santa can move "up", "down", "left", and "right" with one position each time. 
    These will be the commands that you receive. 
    """
    if presents == 0:
        break

    command = input()

    # If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
    if command == 'Christmas morning':
        break

    next_house = matrix.next_position(direction=command,
                                      current_row=matrix.find_coordinates_of_objects("S")[0][0],
                                      current_col=matrix.find_coordinates_of_objects("S")[0][1],
                                      check_if_valid=True)

    # if Santa reaches a house with a naughty kid, he doesn't drop a present.
    if next_house and (matrix.data[next_house[0]][next_house[1]] in ["X", '-']):
        matrix.data[next_house[0]][next_house[1]] = "S"
        matrix.data[santa[0]][santa[1]] = "-"
        santa = next_house

    # If he moves to a house with a nice kid, the kid receives a present:
    elif next_house and matrix.data[next_house[0]][next_house[1]] == "V":
        matrix.data[next_house[0]][next_house[1]] = "S"
        matrix.data[santa[0]][santa[1]] = "-"
        santa = next_house
        presents -= 1
        given_presents += 1

    # If the command sends Santa to a cell marked with "C",
    # Santa eats cookies and becomes happy and extra generous to all the kids around him *
    elif next_house and matrix.data[next_house[0]][next_house[1]] == "C":
        matrix.data[santa[0]][santa[1]] = "-"
        matrix.data[next_house[0]][next_house[1]] = "S"
        santa = next_house
        for direction in ['left', 'right', 'up', 'down']:
            extra_house_r = matrix.delta[direction][0] + santa[0]
            extra_house_c = matrix.delta[direction][1] + santa[1]
            if matrix.data[extra_house_r][extra_house_c] in ['X', 'V'] and presents > 0:
                # We have a kid there
                presents -= 1
                if  matrix.data[extra_house_r][extra_house_c] == 'V':
                    given_presents += 1
                matrix.data[extra_house_r][extra_house_c] = '-'
                if presents == 0:
                    break

count_good_kids = len(matrix.find_coordinates_of_objects('V'))

if presents == 0 and count_good_kids > 0:
    print(f"Santa ran out of presents!")
print(matrix)
if count_good_kids == 0:
    print(f"Good job, Santa! {given_presents} happy nice kid/s.")
else:
    print(f"No presents for {count_good_kids} nice kid/s.")
