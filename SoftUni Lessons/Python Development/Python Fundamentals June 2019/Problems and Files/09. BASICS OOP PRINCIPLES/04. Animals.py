"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1556#3

SUPyF Basics OOP Principles - 04. Animals

Problem:
Create a hierarchy of Animals. Your program should have three different animals – Dog, Frog and Cat.
Deeper in the hierarchy you should have two additional classes
– Kitten and Tomcat. Kittens are female and Tomcats are male!
All types of animals should be able to produce some kind of sound (ProduceSound()).
For example, the dog should be able to bark.
Your task is to model the hierarchy and test its functionality.
Create an animal of each kind and make them all produce sound.
You will be given some lines of input. Each two lines will represent an animal.
On the first line will be the type of animal and on the second – the name, the age and the gender.
When the command "Beast!" is given, stop the input and print all the animals in the format shown below.
Output:
•	Print the information for each animal on three lines. On the first line, print: "<AnimalType>"
•	On the second line print: "<Name> <Age> <Gender>"
•	On the third line print the sounds it produces: "<ProduceSound()>"
Constraints:
•	Each Animal should have a name, an age and a gender
•	All input values should not be blank (e.g. name, age and so on…)
•	If you receive an input for the gender of a Tomcat or a Kitten, ignore it but create the animal
•	If the input is invalid for one of the properties, throw an exception with message: "Invalid input!"
•	Each animal should have the functionality to ProduceSound()
•	Here is the type of sound each animal should produce:
o	Dog: "Woof!"
o	Cat: "Meow meow"
o	Frog: "Ribbit"
o	Kittens: "Meow"
o	Tomcat: "MEOW"
Examples:
    Input:
        Cat
        Tom 12 Male
        Dog
        Sharo 132 Male
        Beast!
    Output:
        Cat
        Tom 12 Male
        Meow meow
        Dog
        Sharo 132 Male
        Woof!
---------------------------
    Input:
        Frog
        Kermit 12 Male
        Beast!
    Output:
        Frog
        Kermit 12 Male
        Ribbit
---------------------------
    Input:
        Frog
        Sashko -2 Male
        Frog
        Sashko 2 Male
        Beast!
    Output:
        Invalid input!
        Frog
        Sashko 2 Male
        Ribbit
"""


class Animal:
    def __init__(self, a_type, name, age, gender):
        self.a_type = a_type
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def a_type(self):
        return self._a_type

    @a_type.setter
    def a_type(self, a_type):
        if a_type == "Dog" or a_type == "Cat" or a_type == "Frog" or a_type == "Kitten" or a_type == "Tomcat":
            self._a_type = a_type
        else:
            raise Exception("Invalid input!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 2 and name.isalpha() and name[0].isupper():
            self._name = name
        else:
            raise Exception("Invalid input!")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age.isdigit() and int(age) > 0:
            self._age = age
        else:
            raise Exception("Invalid input!")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if self.a_type == "Kitten":
            self._gender = "Female"
        elif self.a_type == "Tomcat":
            self._gender = "Male"
        elif gender == "Male" or gender == "Female":
            self._gender = gender
        else:
            raise Exception("Invalid input!")

    def sound(self):
        if self.a_type == "Dog":
            sound = "Woof!"
            return sound
        elif self.a_type == "Cat":
            sound = "Meow meow"
            return sound
        elif self.a_type == "Frog":
            sound = "Ribbit"
            return sound
        elif self.a_type == "Kitten":
            sound = "Meow"
            return sound
        elif self.a_type == "Tomcat":
            sound = "MEOW"
            return sound

    def __str__(self):
        return f"{self.a_type}" + "\n" + f"{self.name} {self.age} {self.gender}" + "\n" + f"{self.sound()}"


while True:
    type_animal = input()
    if type_animal == "Beast!":
        break
    animal_data = input().split()
    animal_name = animal_data[0]
    animal_age = animal_data[1]
    animal_gender = animal_data[2]

    try:
        a = Animal(a_type=type_animal, name=animal_name, age=animal_age, gender=animal_gender)
        print(a)
    except Exception as e:
        print(str(e))
