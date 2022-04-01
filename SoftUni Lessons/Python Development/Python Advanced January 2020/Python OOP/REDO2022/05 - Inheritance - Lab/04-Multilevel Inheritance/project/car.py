from project.vehicle import Vehicle


class Car(Vehicle):
    @classmethod
    def drive(cls):
        return f"driving..."
