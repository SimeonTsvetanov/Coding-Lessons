"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#6

SUPyF2 Dict-Exercise - 07. Student Academy

Problem:
Write a program that keeps information about students and their grades.
You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade.
Check if the student already exists and if not, add him. Keep track of all grades for each student.
When you finish reading the data, keep the students with average grade higher than or equal to 4.50.
Order the filtered students by average grade in descending order.
Print the students and their average grade in the following format:
{name} –> {averageGrade}
Format the average grade to the 2nd decimal place.

Examples:
Input:          Output:
5               John -> 5.00
John            George -> 5.00
5.5             Alice -> 4.50
John
4.5
Alice
6
Alice
3
George
5

Input:          Output:
5               Robert -> 6.00
Amanda          Rob -> 5.50
3.5             Christian -> 5.00
Amanda
4
Rob
5.5
Christian
5
Robert
6
"""
academy = {}

for i in range(int(input())):
    student, grade = input(), float(input())
    if student not in academy:
        academy[student] = [grade]
    else:
        academy[student].append(grade)

for student, grades in academy.items():
    academy[student] = (sum(grades) / len(grades))

for student, grade in sorted(academy.items(), key=lambda x: -x[1]):
    if grade >= 4.5:
        print(f"{student} -> {grade:.2f}")


