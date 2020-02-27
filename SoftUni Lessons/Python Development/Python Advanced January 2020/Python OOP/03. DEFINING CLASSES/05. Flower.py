"""
# This is the solution from work at home:
class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        self.water_requirements -= quantity
        if self.water_requirements <= 0:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
"""


# And this is the solution from work in class:
class Flower:
    is_happy = False

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.current_quantity = 0

    def water(self, quantity):
        # This was the first option:
        # self.is_happy = self.water_requirements <= quantity

        # And this is the second one:
        self.current_quantity += quantity
        self.is_happy = self.water_requirements <= self.current_quantity

    def status(self):
        result = f"{self.name} is not happy"
        if self.is_happy:
            result = f"{self.name} is happy"
        return result
