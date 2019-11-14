"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1556#2

SUPyF Basics OOP Principles - 03. Mankind

Problem:
Your task is to model an application. It is very simple.
The mandatory models of our application are 3:  Human, Worker and Student.
The parent class – Human should have first name and last name. Every student has a faculty number.
Every worker has a week salary and work hours per day.
It should be able to calculate the money he earns by an hour. You can see the constraints below.
Input
On the first input line, you will be given info about a single student - a name and faculty number.
On the second input line, you will be given info about a single worker - first name, last name, salary and working hours.
Output
You should print the info about the student first,
followed by a single blank line and after that the info about the worker in the given formats:
- Print the student info in the following format:
    First Name: {student's first name}
    Last Name: {student's last name}
    Faculty number: {student's faculty number}

- Print the worker info in the following format:
    First Name: {worker's first name}
    Last Name: {worker's second name}
    Week Salary: {worker's salary}
    Hours per day: {worker's working hours}
    Salary per hour: {worker's salary per hour}
Print exactly two digits after every double value's decimal separator (e.g. 10.00).
Consider the workweek from Monday to Friday. A faculty number should be consisted only of digits and letters.

Constraints:
-----------------------------------------------------------------------------------------------------------------------
Parameter:        |Constraint                         |Exception Message
-----------------------------------------------------------------------------------------------------------------------
Human first name  |Should start with a capital letter |"Expected upper case letter! Argument: firstName"
Human first name  |Should be more than 3 symbols      |"Expected length at least 4 symbols! Argument: firstName"
Human last name   |Should start with a capital letter |"Expected upper case letter! Argument: lastName"
Human last name   |Should be more than 2 symbols      |"Expected length at least 3 symbols! Argument: lastName "
Human last name   |Should be in range [5..10] symbols |"Invalid faculty number!"
Week salary       |Should be more than 10             |"Expected value mismatch! Argument: weekSalary"
Working hours     |Should be in the range [1..12]     |"Expected value mismatch! Argument: workHoursPerDay"
-----------------------------------------------------------------------------------------------------------------------

Examples:
    Input:
        Ivan Ivanov 08
        Pesho Kirov 1590 10
        Stefo Mk321 0812111
        Ivcho Ivancov 1590 10
    Output:
        Invalid faculty number!
        First Name: Stefo
        Last Name: Mk321
        Faculty number: 0812111

        First Name: Ivcho
        Last Name: Ivancov
        Week Salary: 1590.00
        Hours per day: 10.00
        Salary per hour: 31.80
"""


class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, firstname):
        if firstname[0].isupper():
            self._first_name = firstname
        else:
            raise Exception("Expected upper case letter! Argument: firstName")
        if len(firstname) > 3:
            self._first_name = firstname
        else:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")

    @last_name.setter
    def last_name(self, lastname):
        if lastname[0].isupper():
            self._last_name = lastname
        else:
            raise Exception("Expected upper case letter! Argument: lastName")
        if len(lastname) > 2:
            self._last_name = lastname
        else:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self._faculty_number

    @faculty_number.setter
    def faculty_number(self, faculty_number):
        if 5 <= len(faculty_number) <= 10 and faculty_number.isalnum():
            self._faculty_number = faculty_number
        else:
            raise Exception("Invalid faculty number!")

    def __str__(self):
        return f"First Name: {self.first_name}" + "\n" + f"Last Name: {self.last_name}" + "\n" + \
               f"Faculty number: {self.faculty_number}"


class Worker(Human):
    def __init__(self, first_name, last_name, week_salary, work_hours_per_day):
        Human.__init__(self, first_name, last_name)
        self.week_salary = week_salary
        self.work_hours_per_day = work_hours_per_day
        self.salary_per_hour = week_salary / 5 / work_hours_per_day

    @property
    def week_salary(self):
        return self._week_salary

    @property
    def work_hours_per_day(self):
        return self._work_hours_per_day

    @week_salary.setter
    def week_salary(self, week_salary):
        if week_salary > 10:
            self._week_salary = week_salary
        else:
            raise Exception("Expected value mismatch! Argument: weekSalary")

    @work_hours_per_day.setter
    def work_hours_per_day(self, work_hours_per_day):
        if 1 <= int(work_hours_per_day) <= 12:
            self._work_hours_per_day = work_hours_per_day
        else:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")

    def __str__(self):
        return \
            f"First Name: {self.first_name}" + "\n" + \
            f"Last Name: {self.last_name}" + "\n" + \
            f"Week Salary: {self.week_salary:.2f}" + "\n" + \
            f"Hours per day: {self.work_hours_per_day:.2f}" + "\n" + \
            f"Salary per hour: {self.salary_per_hour:.2f}"


s_d = input().split()
student_first_name = s_d[0]
student_last_name = s_d[1]
student_number = s_d[2]

w_d = input().split()
worker_f_name = w_d[0]
worker_l_name = w_d[1]
worker_week_sel = float(w_d[2])
worker_w_h_p_d = float(w_d[3])

its_ok = False

try:
    st = Student(first_name=student_first_name, last_name=student_last_name, faculty_number=student_number)
    its_ok = True
    wo = Worker(first_name=worker_f_name, last_name=worker_l_name, week_salary=worker_week_sel,
                work_hours_per_day=worker_w_h_p_d)
    if its_ok:
        print(st)
        print()
        print(wo)
except Exception as e:
    print(str(e))
    its_ok = False
