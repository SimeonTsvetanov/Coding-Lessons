"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#2

SUPyF Objects and Classes - 03. Rectangle Position

Problem:
Write a program to read two rectangles {left, top, width, height} and print whether the first is inside the second.
The input is given as two lines, each holding a rectangle, described by 4 integers: left, top, width and height.

Examples:
    Input:          |   Output:
        4 -3 6 4    |       Inside
        2 -3 10 6   |
-------------------------------------
    Input:          |   Output:
        2 -3 10 6    |       Not inside
        4 -5 6 10   |

Hints
    - Create a class Rectangle holding properties Top, Left, Width and Height.
    - Define calculated properties Right and Bottom.
    - Define a method is_inside(rectangle). A rectangle r1 is inside another rectangle r2 when:
        - r1.left ≥ r2.left
        - r1.right ≤ r2.right
        - r1.top ≤ r2.top
        - r1.bottom ≤ r2.bottom
    - Create a method to read a Rectangle.
    - Combine all methods into a single program.
"""


class Rect:
    def __init__(self, left, right, width, height):
        self.left = left
        self.right = right
        self.bottom = right + height
        self.top = left + width

    def is_inside(self, r):
        if self.left >= r.left and self.right <= r.right and self.top <= r.top and self.bottom <= r.bottom:
            return True
        return False


i_1 = [int(item) for item in input().split(" ")]
r1 = Rect(i_1[0], i_1[1], i_1[2], i_1[3])

i_2 = [int(item) for item in input().split(" ")]
r2 = Rect(i_2[0], i_2[1], i_2[2], i_2[3])

if r1.is_inside(r2):
    print("Inside")
else:
    print("Not inside")
