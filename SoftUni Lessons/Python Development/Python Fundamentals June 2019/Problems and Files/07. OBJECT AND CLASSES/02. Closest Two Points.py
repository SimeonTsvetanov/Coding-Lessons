"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#1

SUPyF Objects and Classes - 02. Closest Two Points

Problem:
Write a program to read n points and find the closest two of them.

Input:
    The input holds the number of points n and n lines, each holding a point {X and Y coordinate}.
Output
    - The output holds the shortest distance and the closest two points.
    - If several pairs of points are equally close, print the first of them (from top to bottom).

Hints:
    - Use the class Point you created in the previous task.
    - Create an array  points that will keep all points.
    - Create a method find_closest_points(points) that will check distance between every two pairs from the array of
    points and returns the two closest points in a new array.
    - Print the closest distance and the coordinates of the two closest points.
"""

import math
import sys


class ClosePoints:
    def __init__(self, first, second, diff):
        self.first = first
        self.second = second
        self.diff = diff


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, second_point):
        a = int(math.fabs(self.x - second_point.x))
        b = int(math.fabs(self.y - second_point.y))
        result = math.sqrt((a * a) + (b * b))
        return result


count = int(input())

points = list()
closest_points = list()

for i in range(count):
    In = input().split(" ")
    points.append(Point(int(In[0]), int(In[1])))

closest = sys.maxsize
close_points = None

for p in range(len(points)):
    for i in range(len(points)):
        if p == i:
            continue
        distance = points[p].calculate_distance(points[i])
        if distance < closest:
            closest = distance
            close_points = ClosePoints(points[p], points[i], distance)

print(f"{close_points.diff:.3f}")
print(f"({close_points.first.x}, {close_points.first.y})")
print(f"({close_points.second.x}, {close_points.second.y})")
