"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#7

SUPyF Objects and Classes - 08. Boxes

Problem:
Create a class Box, which will represent a rectangular box. The Box should have UpperLeft (Point), UpperRight (Point),
 BottomLeft (Point), BottomRight (Point).
Create, or use from the Lab, the class Point which has X (int) and Y (int) – coordinates in 2D space.
Move the CalculateDistance() method in the Point class, exactly as it is.
Then use “Point.CalculateDistance(point1, point2)” signature, to use the method.
Create 2 methods in the Box class:
CalculatePerimeter(width, height)
CalculateArea(width, height).
Make them return integers, representing the perimeter and area of the box.
The formulas are respectively – (2 * Width + 2 * Height) and (Width * Height).
The Width is the distance between the UpperLeft and the UpperRight Points,
and ALSO – the Bottomleft and the BottomRight Points.
The Height is the distance between the UpperLeft and the BottomLeft Points,
and ALSO – the UpperRight and the BottomRight Points.
You will receive several input lines in the following format:
{X1}:{Y1} | {X2}:{Y2} | {X3}:{Y3} | {X4}:{Y4}
Those will be the coordinates to UpperLeft, UpperRight, BottomLeft and BottomRight (IN THE SAME ORDER).
When you receive the command “end”. You must print all Boxes in the following format:
“Box: {width}, {height}
 Perimeter: {perimeter}
 Area: {area}”
Examples:
    Input:
        0:2 | 2:2 | 0:0 | 2:0
        -3:0 | 0:0 | -3:-3 | 0:-3
        -2:2 | 2:2 | -2:-2 | 2:-2
        end
    Output:
        Box: 2, 2
        Perimeter: 8
        Area: 4
        Box: 3, 3
        Perimeter: 12
        Area: 9
        Box: 4, 4
        Perimeter: 16
        Area: 16
"""


import math


class Box:
    def __init__(self, width, height, perimeter, area):
        self.width = width
        self.height = height
        self.perimeter = perimeter
        self.area = area


def calculate_distance(u_l, u_r, b_l, b_r):
    width = math.sqrt(math.pow(u_l[0] - u_r[0], 2) + math.pow(u_l[1] - u_r[1], 2))
    height = math.sqrt(math.pow(u_l[0] - b_l[0], 2) + math.pow(u_l[1] - b_l[1], 2))
    perimeter = 2 * width + 2 * height
    area = width * height
    current_box = Box(width, height, perimeter, area)
    global all_boxes
    all_boxes += [current_box]


all_boxes = []

while True:
    inp = input()
    if inp == "end":
        break
    data = [item for item in inp.split(" | ")]
    u_l_ = [int(item) for item in data[0].split(":")]
    u_r_ = [int(item) for item in data[1].split(":")]
    b_l_ = [int(item) for item in data[2].split(":")]
    b_r_ = [int(item) for item in data[3].split(":")]
    calculate_distance(u_l_, u_r_, b_l_, b_r_)

for box in all_boxes:
    print(f"Box: {int(box.width)}, {int(box.height)}")
    print(f"Perimeter: {int(box.perimeter)}")
    print(f"Area: {int(box.area)}")
