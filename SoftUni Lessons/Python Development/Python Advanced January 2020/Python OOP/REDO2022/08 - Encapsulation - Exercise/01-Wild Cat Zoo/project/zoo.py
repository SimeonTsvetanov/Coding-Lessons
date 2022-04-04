from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity < (len(self.animals) + 1):
            return "Not enough space for animal"
        if self.__budget - price < 0:
            return "Not enough budget"
        if animal.__class__.__name__ in ['Lion', 'Tiger', 'Cheetah']:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if (len(self.workers) + 1 <= self.__workers_capacity) and worker.__class__.__name__ in ['Keeper', 'Caretaker', 'Vet']:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        found = [w for w in self.workers if w.name == worker_name]
        if found:
            self.workers.remove(found[0])
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount = sum([w.salary for w in self.workers])
        if self.__budget - amount >= 0:
            self.__budget -= amount
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount = sum([a.money_for_care for a in self.animals])
        if self.__budget - amount >= 0:
            self.__budget -= amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        result = f'You have {len(self.animals)} animals\n'
        result += f"----- {len(lions)} Lions:\n"
        for leo in lions:
            result += f"{str(leo)}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tigi in tigers:
            result += f"{str(tigi)}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for chity in cheetahs:
            result += f"{str(chity)}\n"
        return result[:-1]

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{str(k)}\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            result += f"{str(c)}\n"
        result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            result += f"{str(v)}\n"
        return result[:-1]
