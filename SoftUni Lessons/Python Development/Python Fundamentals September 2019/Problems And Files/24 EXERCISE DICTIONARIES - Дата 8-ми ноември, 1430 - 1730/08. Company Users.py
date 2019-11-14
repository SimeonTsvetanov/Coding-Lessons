"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#7

SUPyF2 Dict-Exercise - 08. Company Users

Problem:
Write a program that keeps information about companies and their employees.
You will be receiving a company name and an employee's id, until you receive the command "End" command.
Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
When you finish reading the data, order the companies by the name in ascending order.
Print the company name and each employee's id in the following format:
{companyName}
-- {id1}
-- {id2}
-- {idN}
Input / Constraints
•	Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
•	The input always will be valid.

Examples:
Input:
SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End

Output:
HP
-- BB12345
Microsoft
-- CC12345
SoftUni
-- AA12345
-- BB12345

Input:
SoftUni -> AA12345
SoftUni -> CC12344
Lenovo -> XX23456
SoftUni -> AA12345
Movement -> DD11111
End

Output:
Lenovo
-- XX23456
Movement
-- DD11111
SoftUni
-- AA12345
-- CC12344
"""

companies = {}

while True:
    command = input()
    if command == "End":
        break
    company, employee_id = command.split(" -> ")
    if company not in companies:
        companies[company] = [employee_id]
    else:
        if employee_id not in companies[company]:
            companies[company] += [employee_id]

for company, employees in sorted(companies.items()):
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
