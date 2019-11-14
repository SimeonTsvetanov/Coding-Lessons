"""
Objects and Classes
Проверка: https://judge.softuni.bg/Contests/Practice/Index/950#0

SUPyF Objects and Classes - 01. Distance Between Points

Problem:
1.	Distance Between Points
Write a method to calculate the distance between two points p1 {x1, y1} and p2 {x2, y2}.
Write a program to read two points (given as two integers) and print the Euclidean distance between them.
Result, needs to be formatted with :.3f

Examples:
Input: |Output:|/    Input: |Output:|/    Input:  |Output: |/
3 4    |5.000  |/    3 4    |2.000  |/    8 -2    |11.402  |/
6 8    |       |/    5 4    |       |/    -1 5    |        |/
"""
import math


class Point:
    def __init__(self, data):
        self.data = [int(item) for item in data.split()]
        self.x = self.data[0]
        self.y = self.data[1]


def calculate(d_1, d_2):
    distance = math.sqrt(math.pow(d_1.x - d_2.x, 2) + math.pow(d_1.y - d_2.y, 2))
    return f"{distance:.3f}"


p1 = Point(input())
p2 = Point(input())

print(calculate(p1, p2))


"""
From Classes:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculate(point_1: Point, point_2: Point):
    side_a = abs(point_1.x - point_2.x)
    side_b = abs(point_1.y - point_2.y)
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    return side_c


def create_point(x, y):
    point = Point(x, y)
    return point


x1, y1 = [int(item) for item in input().split()]
x2, y2 = [int(item) for item in input().split()]

point_1 = create_point(x1, y1)
point_2 = create_point(x2, y2)

distance = calculate(point_1, point_2)

print(f"{distance:.3f}")
"""