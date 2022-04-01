from project.animal import Animal


class Dog(Animal):
    @classmethod
    def bark(cls):
        return "barking..."
