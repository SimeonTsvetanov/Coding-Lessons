"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#5

SUPyF2 Dict-Exercise - 06. Courses

Problem:
Write a program that keeps information about courses. Each course has a name and registered students.
You will be receiving a course name and a student name, until you receive the command "end".
Check if such course already exists, and if not, add the course. Register the user into the course.
When you receive the command "end", print the courses with their names and total registered users,
ordered by the count of registered users in descending order.
For each contest print the registered users ordered by name in ascending order.

Input:
•	Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".
•	The product data is always delimited by " : ".
Output:
•	Print the information about each course in the following the format:
"{courseName}: {registeredStudents}"
•	Print the information about each student, in the following the format:
"-- {studentName}"

Examples:
Input:
Programming Fundamentals : John Smith
Programming Fundamentals : Linda Johnson
JS Core : Will Wilson
Java Advanced : Harrison White
end

Output:
Programming Fundamentals: 2
-- John Smith
-- Linda Johnson
JS Core: 1
-- Will Wilson
Java Advanced: 1
-- Harrison White

Input:
Algorithms : Jay Moore
Programming Basics : Martin Taylor
Python Fundamentals : John Anderson
Python Fundamentals : Andrew Robinson
Algorithms : Bob Jackson
Python Fundamentals : Clark Lewis
end

Output:
Python Fundamentals: 3
-- Andrew Robinson
-- Clark Lewis
-- John Anderson
Algorithms: 2
-- Bob Jackson
-- Jay Moore
Programming Basics: 1
-- Martin Taylor
"""

courses = {}

while True:
    command = input()
    if command == "end":
        break
    course, student = command.split(" : ")
    if course in courses:
        courses[course].append(student)
    else:
        courses[course] = [student]

for course, students in sorted(courses.items(), key=lambda x: (len(x[1])), reverse=True):
    print(f"{course}: {len(courses[course])}")
    for student in sorted(students):
        print(f"-- {student}")
