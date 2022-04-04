from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine):
        self.__caffeine = caffeine
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)

    @property
    def caffeine(self):
        return self.__caffeine
