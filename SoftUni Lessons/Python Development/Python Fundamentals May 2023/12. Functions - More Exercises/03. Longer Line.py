# WTF This task was stupid complicated!!!

import math


def get_input():
    x1, y1, x2, y2, x_1, y_1, x_2, y_2 = \
        float(input()), float(input()), float(input()), float(input()), \
        float(input()), float(input()), float(input()), float(input())
    return x1, y1, x2, y2, x_1, y_1, x_2, y_2


def get_distance(x1, y1, x2, y2):
        y = x2 - x1
        x = y2 - y1

        return math.sqrt(x * x + y * y)


def calculate(x1, y1, x2, y2, x_1, y_1, x_2, y_2):
    distance_a = get_distance(x1, y1, x2, y2)
    distance_b = get_distance(x_1, y_1, x_2, y_2)

    if distance_a >= distance_b:
        distance_x1_y1 = get_distance(x1, y1, 0, 0)
        distance_x2_y2 = get_distance(x2, y2, 0, 0)
        if distance_x1_y1 <= distance_x2_y2:
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        else:
            return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"

    else:
        distance_x_1_y_1 = get_distance(x_1, y_1, 0, 0)
        distance_x_2_y_2 = get_distance(x_2, y_2, 0, 0)
        if distance_x_1_y_1 <= distance_x_2_y_2:
            return f"({math.floor(x_1)}, {math.floor(y_1)})({math.floor(x_2)}, {math.floor(y_2)})"
        else:
            return f"({math.floor(x_2)}, {math.floor(y_2)})({math.floor(x_1)}, {math.floor(y_1)})"


def run():
    x1, y1, x2, y2 , x_1, y_1, x_2, y_2 = get_input()
    print(calculate(x1, y1, x2, y2, x_1, y_1, x_2, y_2))


if __name__ == '__main__':
    run()
