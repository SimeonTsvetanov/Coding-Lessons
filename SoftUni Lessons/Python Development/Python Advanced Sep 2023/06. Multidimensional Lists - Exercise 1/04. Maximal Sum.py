# Uncomment the solution you would like to use on the bottom.

def solution_one():
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

    rows, cols = list(map(int, input().split()))
    matrix = Matrix(rows=rows, type_data=int, separator=" ")
    total = 0
    result = ''
    for row in range(rows - 2):
        for col in range(cols - 2):
            a = matrix.data[row][col]
            b = matrix.data[row][col + 1]
            c = matrix.data[row][col + 2]
            d = matrix.data[row + 1][col]
            e = matrix.data[row + 1][col + 1]
            f = matrix.data[row + 1][col + 2]
            g = matrix.data[row + 2][col]
            h = matrix.data[row + 2][col + 1]
            i = matrix.data[row + 2][col + 2]
            if sum([a, b, c, d, e, f, g, h, i]) >= total:
                total = sum([a, b, c, d, e, f, g, h, i])
                result = f"{a} {b} {c}\n{d} {e} {f}\n{g} {h} {i}\n"

    print(f"Sum = {total}")
    print(result)

def solution_two():
    row, col = [int(x) for x in input().split(' ')]
    m = [[int(x) for x in input().split(' ')] for r in range(row)]

    square = []
    max_sum = 0

    for r in range(len(m) - 2):
        for c in range(len(m[r]) - 2):
            current_square = [
                m[r][c], m[r][c + 1], m[r][c + 2],
                m[r + 1][c], m[r + 1][c + 1], m[r + 1][c + 2],
                m[r + 2][c], m[r + 2][c + 1], m[r + 2][c + 2]
            ]
            current_sum = sum(current_square)

            # TODO WTF The description of the task says:
            # There will be no case with two or more 3x3 squares with equal maximal sum
            # Yet there is and if you don't count it, Judge will give you 80/100 :D
            if current_sum >= max_sum:
                square = current_square
                max_sum = current_sum

    print(f"Sum = {max_sum}")
    print(
        f"{square[0]} {square[1]} {square[2]}\n{square[3]} {square[4]} {square[5]}\n{square[6]} {square[7]} {square[8]}")


# solution_one()
# solution_two()
