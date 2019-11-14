"""
Objects and Classes - Exericse
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1734#4

SUPyF2 Objects/Classes-Exericse - 05. Class

Problem:
Create a class Class. The __init__ method should receive the name of the class.
It should also have 2 lists (students and grades). Create a class attribute __students_count equal to 22.
The class should also have 3 additional methods:
•	add_student(name, grade) - if there is space in the class, add the student and the grade in the two lists
•	get_average_grade() - returns the average of all existing grades formatted to the second decimal point
•	__repr__ - returns the string (single line):
"The students in {class_name}: {students}. Average grade: {get_average_grade()}". The students must be seperated by ", "

Example:
Test Code:
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

Output:
The students in 11B: Peter, George, Amy. Average grade: 4.77

#TODO Judge result - 75/100
"""


class Class:

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []
        self.__students_count = 22

    def add_student(self, name: str, grade: float):
        if len(self.students) < self.__students_count:
            self.students += [name]
            self.grades += [grade]

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")

a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy2", 3.50)
a_class.add_student("Peter3", 4.80)
a_class.add_student("George4", 6.00)
a_class.add_student("Amy5", 3.50)
print(a_class)

b_class = Class("11B")
b_class.add_student("Peter", 4.80)
b_class.add_student("George", 6.00)
b_class.add_student("Amy", 3.50)
print(b_class)

