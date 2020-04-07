from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["chicken egg", "quail egg"]:
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
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients
