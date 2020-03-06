"""
Create three classes named Person, Employee and Teacher.
Person with a single public method sleep() that returns: "sleeping..."
Employee with a single public method get_fired() that returns: "fired..."
Teacher with a single public method teach() that returns: "teaching..."
Teacher should inherit from Person and Employee.

"""


class Person:
    """Class Person with a single public method sleep() that returns: 'sleeping...' """
    @classmethod
    def sleep(cls):
        return "sleeping..."


class Employee:
    """Class Employee with a single public method get_fired() that returns: 'fired...' """
    @classmethod
    def get_fired(cls):
        return "fired..."


class Teacher(Person, Employee):
    """
    Class Teacher should inherit from Person and Employee.
    and it has a  single public method teach() that returns: "teaching..."
    """
    @classmethod
    def teach(cls):
        return "teaching..."
