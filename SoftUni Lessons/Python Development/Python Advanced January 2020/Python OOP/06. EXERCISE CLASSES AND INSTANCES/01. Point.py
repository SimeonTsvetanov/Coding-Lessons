import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        """changes the x value of the point"""
        self.x = new_x

    def set_y(self, new_y):
        """changes the y value of the point"""
        self.y = new_y

    def distance(self, x2, y2):
        """returns the distance between the point and the provided coordinates"""
        return math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
