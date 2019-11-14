"""
Functions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1727#4

SUPyF2 Functions-Lab - 05. Calculate Rectangle Area
Problem:
Create a function that calculates and returns the area of a rectangle by given width and height:

Examples:

Input:	Output:
3
4	    12

6
2	    12
"""


def rectangle_area(side_a, side_b):
    return f"{(side_a * side_b)}"


print(rectangle_area(int(input()), int(input())))
