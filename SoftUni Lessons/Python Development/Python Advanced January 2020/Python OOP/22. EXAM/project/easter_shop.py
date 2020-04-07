# from project.factory.factory import Factory
from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        """makes a chocolate in the chocolate_factory and add the chocolate to the storage"""
        if recipe not in self.storage:
            self.storage[recipe] = 1
        else:
            self.storage[recipe] += 1
        self.chocolate_factory.make_chocolate(recipe)

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.ingredients and color in self.paint_factory.ingredients:
            # if self.egg_factory.ingredients[egg_type] >= 1 and self.paint_factory.ingredients[color] >= 1:
            key = f"{color} {egg_type}"
            self.egg_factory.remove_ingredient(egg_type, 1)
            self.paint_factory.remove_ingredient(color, 1)
            if key not in self.storage:
                self.storage[key] = 1
            else:
                self.storage[key] += 1
            # else:
            #     raise ValueError("Invalid commands")
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        """
        Returns a string representation of the shop in the following format
        Shop name: {name}
        Shop Storage:
        {item1 name}: {item1 quantity}
        """
        result = ""
        result += f"Shop name: {self.name}\n"
        result += f"Shop Storage:\n"
        for item, quantity in self.storage.items():
            result += f"{item}: {quantity}\n"
        return result
