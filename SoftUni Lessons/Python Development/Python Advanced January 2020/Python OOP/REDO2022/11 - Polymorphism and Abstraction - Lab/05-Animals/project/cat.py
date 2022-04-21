from project.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"


# cat = Cat("Johnny", 7, "Male")
# print(cat.make_sound())
# print(cat)
