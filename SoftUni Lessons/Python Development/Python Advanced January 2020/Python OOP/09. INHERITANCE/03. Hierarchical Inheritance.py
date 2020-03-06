"""
Create three classes named Animal, Dog and Cat.
Animal with a single public method eat() that returns: "eating..."
Dog with a single public method bark() that returns: "barking..."
Cat with a single public method meow() that returns: "meowing..."
Dog and Cat should inherit from Animal.
"""


class Animal:
    @classmethod
    def eat(cls):
        return "eating..."


class Dog(Animal):  # Inherits Animal
    @classmethod
    def bark(cls):
        return "barking..."


class Cat(Animal):  # Inherits Animal
    @classmethod
    def meow(cls):
        return "meowing..."
