from abc import ABC, abstractmethod
from project.animals.animal import Animal
from project.food import Food
from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    GETTING_FAT = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food) in [Vegetable, Fruit]:
            self.weight += (Mouse.GETTING_FAT * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    GETTING_FAT = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food) == Meat:
            self.weight += (Dog.GETTING_FAT * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    GETTING_FAT = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food) in [Vegetable, Meat]:
            self.weight += (Cat.GETTING_FAT * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    GETTING_FAT = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food) == Meat:
            self.weight += (Tiger.GETTING_FAT * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
