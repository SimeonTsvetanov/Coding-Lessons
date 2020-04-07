from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)
        self.recipes = {}  # empty upon initialization
        self.products = {}  # empty upon initialization

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            if self.can_add(quantity):
                if ingredient_type not in self.ingredients:
                    self.ingredients[ingredient_type] = 0  # First we create the New Type
                self.ingredients[ingredient_type] += quantity  # Then we add the quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients:
            if self.ingredients[ingredient_type] - quantity >= 0:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError("Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes:
            for ingredient, value in self.recipes[recipe_name].items():
                self.remove_ingredient(ingredient, value)

            if recipe_name not in self.products:
                self.products[recipe_name] = 1
            else:
                self.products[recipe_name] += 1
        else:
            raise TypeError("No such recipe")
