"""
Create two classes named Animal and Dog.
Animal with a single public method eat() that returns: "eating…"
Dog with a single public method bark() that returns: "barking…"
Dog should inherit from Animal.
"""


class Animal:
    """This is class Animal with a single public method eat() that returns: 'eating…' """
    @classmethod
    def eat(cls):
        return "eating..."


class Dog(Animal):
    """
    Class Dog which inherits the class Animal
    and it has  single public method bark() that returns: 'barking…'
    """
    @classmethod
    def bark(cls):
        return "barking..."
