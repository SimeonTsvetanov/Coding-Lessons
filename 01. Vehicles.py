from abc import ABC, abstractmethod


class Vehicle(ABC):
    """There is no point of this class .... what so ever :D"""
    @abstractmethod
    def drive(self, kilometers):
        pass

    @abstractmethod
    def refuel(self, volume):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, kilometers):
        needed_fuel = (kilometers * self.fuel_consumption) + (kilometers * 0.9)  # Summer reasons
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, volume):
        self.fuel_quantity += volume


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, kilometers):
        needed_fuel = (kilometers * self.fuel_consumption) + (kilometers * 1.6)  # Air conditioners suck
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, volume):
        self.fuel_quantity += (volume * 0.95)  # adds only 95% of the given fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
