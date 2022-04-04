from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value:
            self.__dough = value
        else:
            raise ValueError("You should add dough to the pizza")

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value > 0:
            self.__toppings_capacity = value
        else:
            raise ValueError("The topping's capacity cannot be less or equal to zero")

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return sum([w for t, w in self.toppings.items()]) + self.dough.weight

