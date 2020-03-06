class Lion:
    def __init__(self, name: str, gender: str, age: int):
        """set all the attributes to the given ones"""
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Lion"

    @classmethod
    def get_needs(cls):
        """returns the number 50 (amount of money needed to tend the animal)"""
        return 50

    def __repr__(self):
        """returns string representation of the lion in the format: """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:
    def __init__(self, name: str, gender: str, age: int):
        """set all the attributes to the given ones"""
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Tiger"

    @classmethod
    def get_needs(cls):
        """returns the number 45 (amount of money needed to tend the animal)"""
        return 45

    def __repr__(self):
        """returns string representation of the lion in the format: """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:
    def __init__(self, name: str, gender: str, age: int):
        """set all the attributes to the given ones"""
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Cheetah"

    @classmethod
    def get_needs(cls):
        """returns the number 60 (amount of money needed to tend the animal)"""
        return 60

    def __repr__(self):
        """returns string representation of the lion in the format: """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:
    def __init__(self, name: str, age: int, salary: int):
        """set all the attributes to the given ones"""
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Keeper"

    def __repr__(self):
        """returns string representation of the keeper in the format: """
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:
    def __init__(self, name: str, age: int, salary: int):
        """set all the attributes to the given ones"""
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Caretaker"

    def __repr__(self):
        """returns string representation of the keeper in the format: """
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:
    def __init__(self, name: str, age: int, salary: int):
        """set all the attributes to the given ones"""
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Vet"

    def __repr__(self):
        """returns string representation of the keeper in the format: """
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if (self.__budget - price >= 0) and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.type} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and (self.__budget - price < 0):
            return f"Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.type} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"  # There was double space here

    def pay_workers(self):
        money_needed = 0
        for worker in self.workers:
            money_needed += worker.salary
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = 0
        for animal in self.animals:
            money_needed += animal.get_needs()
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result_string = ""
        result_string += f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.type == "Lion":
                lions.append(animal)
            elif animal.type == "Tiger":
                tigers.append(animal)
            elif animal.type == "Cheetah":
                cheetahs.append(animal)

        result_string += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result_string += f"{lion.__repr__()}\n"

        result_string += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result_string += f"{tiger.__repr__()}\n"

        result_string += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result_string += f"{cheetah.__repr__()}\n"

        return result_string

    def workers_status(self):
        result_string = ""
        result_string += f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.type == "Keeper":
                keepers.append(worker)
            elif worker.type == "Caretaker":
                caretakers.append(worker)
            elif worker.type == "Vet":
                vets.append(worker)

        result_string += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result_string += f"{keeper.__repr__()}\n"

        result_string += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result_string += f"{caretaker.__repr__()}\n"

        result_string += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result_string += f"{vet.__repr__()}\n"
        return result_string
