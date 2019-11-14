"""
Functions - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1729#1

SUPyF2 Functions-More-Exercises - 02. Center Point

Problem:
You are given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2 and Y2.
Create a method that prints the point that is closest to the center of the coordinate system (0, 0) in the
format (X, Y). If the points are on a same distance from the center, print only the first one.
Examples
Input	Output
2       (-1, 2)
4
-1
2
"""
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculate(d_1, d_2):
    distance_1 = abs(math.sqrt(math.pow(d_1.x - 0, 2) + math.pow(d_1.y - 0, 2)))
    distance_2 = abs(math.sqrt(math.pow(0 - d_2.x, 2) + math.pow(0 - d_2.y, 2)))
    if distance_1 <= distance_2:
        print(f"({int(d_1.x)}, {int(d_1.y)})")
    else:
        print(f"({int(d_2.x)}, {int(d_2.y)})")


p1 = Point(float(input()), float(input()))
p2 = Point(float(input()), float(input()))

calculate(p1, p2)


