"""
Lists Advanced - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1730#1

SUPyF2 Lists-Advanced-Lab - 02. To-do List

Problem:
You will receive a to-do-notes until you get the command "End".
The notes will be in the format: "{importance}-{value}". Return the list of to-do-notes sorted by importance.
The maximum importance will be 10
Hint
•	Use the insert() method

Examples:

Input:	            Output
2-Walk the dog      ['Drink coffee', 'Walk the dog', 'Work', Dinner']
1-Drink coffee
6-Dinner
5-Work
End
"""
commands = []

while True:
    command = input()
    if command == "End":
        break
    commands.append(command)

notes = ["None"] * len(commands)

for note in commands:
    note = note.split("-")
    note_priority = int(note[0])
    note_message = note[1]
    notes.insert(note_priority, note_message)

print([note for note in notes if note != "None"])
