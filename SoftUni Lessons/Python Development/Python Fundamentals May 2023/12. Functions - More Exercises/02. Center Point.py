import math


def get_input():
    x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
    return x1, y1, x2, y2


def get_distance(x1, y1, x2, y2):
        y = x2 - x1
        x = y2 - y1

        return math.sqrt(x * x + y * y)


def calculate(x1, y1, x2, y2):
    distance_a = get_distance(x1, y1, 0, 0)
    distance_b = get_distance(x2, y2, 0, 0)
    if distance_a <= distance_b:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


def run():
    x1, y1, x2, y2 = get_input()
    print(calculate(x1, y1, x2, y2))


if __name__ == '__main__':
    run()
