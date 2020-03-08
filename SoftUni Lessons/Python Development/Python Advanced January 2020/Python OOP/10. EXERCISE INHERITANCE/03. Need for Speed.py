class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = int(horse_power)

    def drive(self, kilometers):
        needed_fuel = kilometers * self.fuel_consumption
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel


class Motorcycle(Vehicle):
    pass


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8


class CrossMotorcycle(Motorcycle):
    pass


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3


class FamilyCar(Car):
    pass


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
