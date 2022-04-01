from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        Food.__init__(self, expiration_date)
        self.name = name
