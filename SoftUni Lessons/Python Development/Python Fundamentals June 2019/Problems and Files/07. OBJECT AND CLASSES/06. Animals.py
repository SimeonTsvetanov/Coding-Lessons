"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#5

SUPyF Objects and Classes - 06. Animals

Problem:

You have been given the task to create classes for several sophisticated animals.
Create a class Dog which has a name (string), age (int) and number_of_legs (int).
Create a class Cat which has a name (string), age (int) and intelligence_quotient (int).
Create a class Snake which has a name (string), age(int) and cruelty_coefficient (int).
Create a method in each class which is called produce_sound(). The method should print on the console a string depending
 on the class:
    - If it’s a Dog, you should print “I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.”
    - It it’s a Cat, you should print “I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.”
    - If it’s a Snake, you should print:
        “I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.”
Now for the real deal. You will receive several input commands, which will register animals or make them produce sounds,
until you receive the command “I’m your Huckleberry”.
The commands will be in the following format:
{class} {name} {age} {parameter}
The class will be either “Dog”, “Cat” or “Snake”. The name will be a simple string,
which can contain any ASCII character BUT space. The age will be an integer. The parameter, will be an integer.
Depending on the class it would either be number of legs, IQ, or cruelty coefficient.
Register each animal, and keep them in collections, by your choice, so that you can ACCESS THEM BY NAME.
You will most likely need 3 collections, to store the different animals inside them.
Between the register commands you might receive a command in the following format:
talk {name}
You must then make the animal with the given name, produce a sound.

When you receive the ending command, you should print every animal in the following format:
•	If it’s a Dog, you should print “Dog: {name}, Age: {age}, Number Of Legs: {numberOfLegs}”
•	It it’s a Cat, you should print “Cat: {name}, Age: {age}, IQ: {intelligenceQuotient}”
•	If it’s a Snake, you should print “Snake: {name}, Age: {age}, Cruelty: {crueltyCoefficient}”
Print first the Dogs, then the Cats, and lastly – The Snakes.

Constraints
-   You can assume that there will be no duplicate names (even in different animals).
-   All input data will be valid. There will be no invalid input lines.
-   The name in the talk command, will always be existent.

Examples:
------------------------------------------------------------------------------------
    Input:
Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry
    Output:
I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.
I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.
Dog: Sharo, Age: 3, Number Of Legs: 4
Cat: Garfield, Age: 5, IQ: 200
Snake: Alex, Age: 25, Cruelty: 1000
------------------------------------------------------------------------------------
    Input:
Dog Bau 5 10
Cat Myau 5 100
Dog Georgi 20 1000
Cat Bojo 4 20
talk Bojo
I'm your Huckleberry
    Output:
I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
Dog: Bau, Age: 5, Number Of Legs: 10
Dog: Georgi, Age: 20, Number Of Legs: 1000
Cat: Myau, Age: 5, IQ: 100
Cat: Bojo, Age: 4, IQ: 20
------------------------------------------------------------------------------------
"""


class Animal:
    def __init__(self, type_of, name, age, extra):
        self.type_of = type_of
        self.name = name
        self.age = age
        self.extra = extra

    def produce_sound(self):
        if self.type_of == "Dog":
            return print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")
        elif self.type_of == "Cat":
            return print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")
        elif self.type_of == "Snake":
            return print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def animal_type_sort(self):
        global animals, dogs, cats, snakes
        animals += [animal]
        if self.type_of == "Dog":
            dogs += [animal]
        elif self.type_of == "Cat":
            cats += [animal]
        elif self.type_of == "Snake":
            snakes += [animal]


animals = []
dogs = []
cats = []
snakes = []

while True:
    inp = input()
    data = [item for item in inp.split(" ")]
    if inp == "I'm your Huckleberry":
        break
    elif data[0] == "talk":
        for animal in animals:
            if animal.name == data[1]:
                animal.produce_sound()
                continue
    else:
        animal = Animal(data[0], data[1], data[2], data[3])
        animal.animal_type_sort()

for dog in dogs:
    print(f"Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.extra}")
for cat in cats:
    print(f"Cat: {cat.name}, Age: {cat.age}, IQ: {cat.extra}")
for snake in snakes:
    print(f"Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.extra}")
