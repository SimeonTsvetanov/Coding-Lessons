class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantiry: int):
        if self.quantity - quantiry >= 0:
            self.quantity -= quantiry

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return self.name
