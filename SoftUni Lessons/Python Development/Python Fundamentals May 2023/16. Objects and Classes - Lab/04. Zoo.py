class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        getattr(self, species).append(name)
        self.__animals += 1

    def get_info(self, species):
        animals = "Mammals" if species == "mammal" else "Fishes" if species == "fish" else "Birds"
        return f"{animals} in {self.name}: {', '.join(getattr(self, species))}\nTotal animals: {Zoo.__animals}"


zoo = Zoo(name=input())

for i in range(int(input())):
    species, name = input().split(' ')
    zoo.add_animal(species, name)

print(zoo.get_info(input()))

