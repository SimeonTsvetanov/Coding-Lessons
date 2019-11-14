"""
Objects and Classes - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1733#1

SUPyF2 Objects/Classes-Lab - 02. Party

Problem:
Create a class Party that only has an attribute called people.
The __init__ method should not accept any parameters.
You will be given names of people (on separate lines) until you receive the command "End".
Use the created class to solve this problem. After you receive the end command print 2 lines:
•	"Going: {people}" - the people should be separated by comma and space ", "
•	"Total: {total_people_going}"
Note: submit all of your code including the class

Examples:
Input:	    Output:
Peter       End	Going: Peter, John, Katy
John        Total: 3
Katy
"""


class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    name = input()
    if name == "End":
        break
    party.people += [name]

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

