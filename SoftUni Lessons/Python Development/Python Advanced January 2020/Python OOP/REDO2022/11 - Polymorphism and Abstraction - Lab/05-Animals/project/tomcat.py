from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return f"Hiss"


# tomcat = Tomcat("Tom", 6)
# print(tomcat.make_sound())
# print(tomcat)
