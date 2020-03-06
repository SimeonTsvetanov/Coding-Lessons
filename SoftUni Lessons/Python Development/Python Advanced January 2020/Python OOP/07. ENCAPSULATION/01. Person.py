class Person:
    """Create a class called Person. Upon initialization it should receive name and age.
    Create private properties (cannot be accessed outside the class) called name and age. Create two instance methods"""
    def __init__(self, name, age):
        """The Constructor will create two private attributes"""
        self.__name = name
        self.__age = age

    def get_name(self):
        """returns the name"""
        return self.__name

    def get_age(self):
        """returns the age"""
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
