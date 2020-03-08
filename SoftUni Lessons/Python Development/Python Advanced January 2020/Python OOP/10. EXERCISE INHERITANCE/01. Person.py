"""
You are asked to model an application for storing data about people.
You should be able to have a Person and a Child. The child derives from the person.
Every person has public attributes name and age. Your task is to model the application.
Create a Child class that inherits Person and has the same constructor definition.
However, do not copy the code from the Person class - reuse the Person class's constructor.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Inherit using super() method
        # Person.__init__(self, name, age)  # Inherit using the normal method
