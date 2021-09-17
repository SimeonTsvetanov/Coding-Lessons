"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1556#0

SUPyF Basics OOP Principles - 01. Person

Problem:
You are asked to model an application for storing data about people. You should be able to have a person and a child.
The child derives from the person. Your task is to model the application. The only constraints are:
-	People should not be able to have a negative age
-	Children should not be able to have an age more than 15.

•	Person – represents the base class by which all of the others are implemented
•	Child - represents a class, which derives from Person.
Note
Your class’s names MUST be the same as the names shown above!!!

Step 2 – Define the fields
Define a field for each property the class should have (e.g. Name, Age)

Step 3 - Define the Properties of a Person
Define the Name and Age properties of a Person.

Step 4 - Define a Constructor
Define a constructor that accepts name and age.

Step 5 - Perform Validations
After you have created a field for each property (e.g. Name and Age),
the next step is to perform validations for each one.
The getter should return the corresponding field’s value and the setter
should validate the input data before setting it. Do this for each property.
Constraints
•	If the age of a person is negative – exception’s message is: "Age must be positive!"
•	If the age of a child is bigger than 15 – exception’s message is: "Child's age must be less than 15!"
•	If the name of a child or a person is no longer than three symbols –
exception’s message is: "Name's length should not be less than 3 symbols!"

Step 6 - Override __str__()
"Name: {self.name}, Age: {self.age}",
And voila! If everything is correct, we can now create Person objects and display information about them.
Step 7 – Create a Child
Create a Child class that inherits Person and has the same constructor definition. However,
do not copy the code from the Person class - reuse the Person class’s constructor.
There is no need to rewrite the Name and Age properties since Child inherits Person and by default has them.

Step 8 – Validate the Child’s setter
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception('Age must be positive!')
        else:
            self._age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        else:
            self._name = name


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 15:
            raise Exception("Child's age must be less than 15!")
        elif age < 0:
            raise Exception('Age must be positive!')
        else:
            self._age = age


name_ = input()
age_ = int(input())

try:
    person = Child(name_, age_)
    print(person.__str__())
except Exception as e:
    print(str(e))

    
def another_solution():
    """ This solution is extremely long but it's just for flexing :)"""

    class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @property
        def type_animal(self):
            return self.__class__.__name__

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, var):
            self.__age = int(var)

    class Dog(Animal):
        def __init__(self, name, age, number_of_legs):
            Animal.__init__(self, name, age)
            self.number_of_legs = number_of_legs
            self.sound = "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

        @property
        def number_of_legs(self):
            return self.__number_of_legs

        @number_of_legs.setter
        def number_of_legs(self, value):
            self.__number_of_legs = int(value)

    class Cat(Animal):
        def __init__(self, name, age, intelligence_quotient):
            Animal.__init__(self, name, age)
            self.intelligence_quotient = intelligence_quotient
            self.sound = "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

        @property
        def intelligence_quotient(self):
            return self.__intelligence_quotient

        @intelligence_quotient.setter
        def intelligence_quotient(self, value):
            self.__intelligence_quotient = int(value)

    class Snake(Animal):
        def __init__(self, name, age, cruelty_coefficient):
            Animal.__init__(self, name, age)
            self.cruelty_coefficient = cruelty_coefficient
            self.sound = "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

        @property
        def cruelty_coefficient(self):
            return self.__cruelty_coefficient

        @cruelty_coefficient.setter
        def cruelty_coefficient(self, value):
            self.__cruelty_coefficient = int(value)

    animals = []

    while True:
        command = input()
        if command == "I'm your Huckleberry":
            break
        elif command.split(" ")[0] == "talk":
            [print(animal.sound) for animal in animals if animal.name == command.split(" ")[1]]
        else:
            class_name, a_name, a_age, parameter = command.split(" ")
            animals.append(eval(class_name)(a_name, a_age, parameter))

    for animal in [a for a in animals if a.type_animal == "Dog"]:
        print(f"Dog: {animal.name}, Age: {animal.age}, Number Of Legs: {animal.number_of_legs}")
    for animal in [a for a in animals if a.type_animal == "Cat"]:
        print(f"Cat: {animal.name}, Age: {animal.age}, IQ: {animal.intelligence_quotient}")
    for animal in [a for a in animals if a.type_animal == "Snake"]:
        print(f"Snake: {animal.name}, Age: {animal.age}, Cruelty: {animal.cruelty_coefficient}")
