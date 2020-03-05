class Circle:
    pi = 3.14  # Class Attribute

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        """changes the radius to the new one given"""
        self.radius = new_radius

    def get_area(self):
        """returns the area of the circle"""
        return Circle.pi * self.radius * self.radius

    def get_circumference(self):
        """returns the circumference of the circle"""
        return 2 * Circle.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
