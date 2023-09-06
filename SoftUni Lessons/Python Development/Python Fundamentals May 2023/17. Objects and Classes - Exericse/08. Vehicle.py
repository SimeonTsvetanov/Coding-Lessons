# Task Description was wrong. at the buy method when we sell the car we need to return the change formatted to the
# second decimal point.

class Vehicle:
    def __init__(self, type: str, model: str, price: float):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str) -> str:
        """
        - If the person has enough money and the vehicle has no owner, returns:
        "Successfully bought a {type}. Change: {change}" and sets the owner to the given one
        - If the money is not enough, return: "Sorry, not enough money"
        - If the car already has an owner, return: "Car already sold"
        :param money: provided money
        :param owner: new owner name
        :return: depending on the outcome!
        """
        if money >= self.price and not self.owner:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.price > money:
            return f"Sorry, not enough money"
        elif self.owner:
            return f"Car already sold"

    def sell(self) -> str:
        """
        o If the car has an owner, set it to None again.
        o Otherwise, return: "Vehicle has no owner"
        """
        if self.owner:
            self.owner = None
        else:
            return f"Vehicle has no owner"

    def __repr__(self):
        """
        :return: If the vehicle has an owner, returns: "{model} {type} is owned by: {owner}".
                 Otherwise, return: "{model} {type} is on sale: {price}"
        """
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type,
model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
