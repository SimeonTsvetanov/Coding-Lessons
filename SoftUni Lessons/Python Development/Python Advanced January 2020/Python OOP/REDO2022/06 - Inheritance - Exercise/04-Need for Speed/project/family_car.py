from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
