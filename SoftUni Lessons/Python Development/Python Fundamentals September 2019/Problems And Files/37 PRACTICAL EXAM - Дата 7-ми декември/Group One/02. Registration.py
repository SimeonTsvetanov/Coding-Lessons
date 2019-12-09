"""
Programming Fundamentals Final Exam - 07 December 2019 Group 1
Check your code here: https://judge.softuni.bg/Contests/1928/Programming-Fundamentals-Final-Exam-07-December-2019-Group-1
name: Registration
"""
import re
pattern = r"^U\$(?P<name>[A-Z][a-z][a-z]+)U\$P\@\$(?P<pass>[a-zA-Z]{5,}[\d]+)P\@\$$"

successful_registrations = 0

for _ in range(int(input())):
    line = input()
    match = re.match(pattern, line)
    if match:
        name = match.group("name")
        password = match.group("pass")
        print(f"Registration was successful")
        print(f"Username: {name}, Password: {password}")
        successful_registrations += 1
    else:
        print(f"Invalid username or password")

print(f"Successful registrations: {successful_registrations}")
