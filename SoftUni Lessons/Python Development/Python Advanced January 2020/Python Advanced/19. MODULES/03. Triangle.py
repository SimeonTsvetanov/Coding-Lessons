def print_triangle(size):
    """
    This function will create and print a triangle looking figure build out of numbers:
    :param size: This is the size of the triangle.
    :return: print the triangle
    """
    triangle = []
    counter = 1
    while counter <= size:
        triangle.append([num for num in range(1, counter + 1)])
        counter += 1
    counter -= 1
    while counter >= 0:
        row = [num for num in range(1, counter)]
        if row:
            triangle.append(row)
        counter -= 1
    [print(f"{'   '.join(str(num) for num in row)}") for row in triangle]


def triangle_drawing(n):
    """
    From work in class
    :param n: The size we want to print
    :return:printing triangle with the asked size
    """
    [print('   '.join(map(str, range(1, row + 2)))) for row in range(n)]
    [print('   '.join(map(str, range(1, row)))) for row in range(n, -2, -1)]


triangle_drawing(5)
