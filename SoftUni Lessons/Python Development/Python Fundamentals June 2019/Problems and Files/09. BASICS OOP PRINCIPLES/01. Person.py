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
