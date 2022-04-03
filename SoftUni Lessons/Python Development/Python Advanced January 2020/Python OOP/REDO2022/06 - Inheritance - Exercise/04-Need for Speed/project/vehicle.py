class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        needed_fuel = self.fuel_consumption * kilometers
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel
