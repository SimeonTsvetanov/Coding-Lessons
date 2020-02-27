"""
# This is the solution from work at home:
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
"""


# And this is the solution from work in class:
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        # This is the first option
        # self.quantity += milliliters
        # self.quantity = min(self.quantity, self.size)

        # And this is the second:
        if self.quantity + milliliters <= self.size:
            return
        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
