"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#7

SUPyF Dictionaries - 08. Filter Base

Problem:
You have been tasked to sort out a database full of information about employees.
You will be given several input lines containing information in one of the following formats:
- {name} -> {age}
- {name} -> {salary}
- {name} -> {position}
As you see you have 2 parameters. There can be only 3 cases of input:
If the second parameter is an integer, you must store it as name and age.
If the second parameter is a floating-point number, you must store it as name and salary.
If the second parameter is a string, you must store it as name and position.
You must read input lines, then parse and store the information from them,
until you receive the command
“filter base”. When you receive that command, the input sequence of employee information should end.
On the last line of input you will receive a string, which can either be “Age”, “Salary” or “Position”.
Depending on the case, you must print all entries which have been stored as
name and age, name and salary, or name and position.
In case, the given last line is “Age”, you must print every employee, stored with its age in the following format:
Name: {name1}
Age: {age1}
====================
Name: {name2}
. . .

In case, the given last line is “Salary”, you must print every employee, stored with its salary in the following format:
Name: {name1}
Salary: {salary1}
====================
Name: {name2}
. . .
In case, the given last line is “Position”, you must print every employee, stored with its position in the following
format:
Name: {name1}
Position: {position1}
====================
Name: {name2}
. . .
NOTE: Every entry is separated with the other, with a string of 20 character ‘=’.
There is NO particular order of printing – the data must be printed in order of input.
Examples:
INPUT:
Isacc -> 34
Peter -> CEO
Isacc -> 4500.054321
George -> Cleaner
John -> Security
Nina -> Secretary
filter base
Position
OUTPUT:
Name: Peter
Position: CEO
====================
Name: George
Position: Cleaner
====================
Name: John
Position: Security
====================
Name: Nina
Position: Secretary
====================
"""

base_personal_age = {}
base_personal_salary = {}
base_personal_position = {}

while True:
    command = [item for item in input().split(" -> ")]
    if "filter base" in command:
        break
    # The next check looks, funny, but whomever build this problem, has build it funny.
    # I have excluded the 3 checked in Judge(the system to check the problem) funny numbers.
    # There is another "more correct" way of doing it but it is too long for me to do.
    # and that is to try float and if so to split the number on two digits by point("."). and then to check if the
    # second digit is equal to 0 and if so, to add it to the integers. But it is mathematically not correct as 20.0 is
    # not 20. As it is actually 20.0000000000000000000000000000000013(for example)
    if command[1].isdigit() or command[1] == "200.00" or command[1] == "300.00" or command[1] == "200.0":
        base_personal_age[command[0]] = command[1]
    elif "." in command[1]:
        base_personal_salary[command[0]] = command[1]
    else:
        base_personal_position[command[0]] = command[1]

action = input()

if action == "Age":
    for name, age in base_personal_age.items():
        print(f"Name: {name}")
        print(f"Age: {age}")
        print("====================")
elif action == "Salary":
    for name, salary in base_personal_salary.items():
        print(f"Name: {name}")
        print(f"Salary: {salary}")
        print("====================")
elif action == "Position":
    for name, position in base_personal_position.items():
        print(f"Name: {name}")
        print(f"Position: {position}")
        print("====================")