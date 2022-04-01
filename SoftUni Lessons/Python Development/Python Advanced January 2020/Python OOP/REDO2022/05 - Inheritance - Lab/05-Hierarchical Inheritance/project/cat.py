from project.animal import Animal


class Cat(Animal):
    @classmethod
    def meow(cls):
        return f"meowing..."
