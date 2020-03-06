class Mammal:
    __kingdom = "animals"  # This is a Private Class Attribute

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        """returns a string in the following format:"""
        return f"{self.name} makes {self.sound}"

    @staticmethod
    def get_kingdom():
        """returns the private kingdom attribute"""
        return Mammal.__kingdom

    def info(self):
        """returns a string in the following format:"""
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
