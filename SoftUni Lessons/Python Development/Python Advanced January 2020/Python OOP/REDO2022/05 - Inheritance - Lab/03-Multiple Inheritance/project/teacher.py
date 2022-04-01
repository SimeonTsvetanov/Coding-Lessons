from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    @classmethod
    def teach(cls):
        return "teaching..."
