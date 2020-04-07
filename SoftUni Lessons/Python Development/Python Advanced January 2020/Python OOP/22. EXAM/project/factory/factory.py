from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        """The __init__ method should receive a name: str, and capacity: int. Set the attributes to the given ones"""
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        """Method should be implemented by the child classes"""
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        """Method, should be implemented by the child classes"""
        pass

    def can_add(self, value: int):
        """returns whether the given amount of product (value) can be added in the ingredients"""
        if self.capacity - sum(self.ingredients.values()) - value >= 0:
            return True
        else:
            return False
