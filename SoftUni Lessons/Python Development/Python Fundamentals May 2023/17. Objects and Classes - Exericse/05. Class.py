class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        """
        adds the student and the grade in the two lists if there is
        free space in the class
        :param name: str
        :param grade: float
        :return:
        """
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self) -> float:
        """
        :return: string returns the average of all existing grades formatted to the second decimal point (as a number)
        """
        return float(f"{(sum(self.grades) / len(self.grades)):.2f}")

    def __repr__(self):
        """
        :return: returns the string (single line):
        The students must be separated by a comma and a space: ", ".
        """
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
