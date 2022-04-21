from abc import ABC, abstractmethod
from project.animals.animal import Animal
from project.food import Food, Vegetable, Fruit, Meat, Seed
from project.animals.animal import Bird


class Owl(Bird):
    GETTING_FAT = 0.25

    def __init__(self, name, weight, wing_size):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += (Owl.GETTING_FAT * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    GETTING_FAT = 0.35

    def __init__(self, name, weight, wing_size):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += (Hen.GETTING_FAT * food.quantity)
        self.food_eaten += food.quantity
