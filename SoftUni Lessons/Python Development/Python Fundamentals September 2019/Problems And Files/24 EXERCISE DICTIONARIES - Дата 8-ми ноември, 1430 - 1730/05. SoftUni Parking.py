"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#4

SUPyF2 Dict-Exercise - 05. SoftUni Parking

Problem:
SoftUni just got a new parking lot. It's so fancy, it even has online parking validation.
Except the online service doesn't work. It can only receive users' data,
but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
Write a program, which validates a parking place for an online service.
Users can register to park and unregister to leave.
The program receives 2 types of commands:
•	"register {username} {licensePlateNumber}":
o	The system only supports one car per user at the moment,
so if a user tries to register another license plate, using the same username, the system should print:
"ERROR: already registered with plate number {licensePlateNumber}"
o	If the aforementioned checks passes successfully, the plate can be registered, so the system should print:
 "{username} registered {licensePlateNumber} successfully"
•	"unregister {username}":
o	If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
o	If the aforementioned check passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license plates in the format:
•	"{username} => {licensePlateNumber}"
Input
•	First line: n – number of commands – integer
•	Next n lines: commands in one of the two possible formats:
o	Register: "register {username} {licensePlateNumber}"
o	Unregister: "unregister {username}"
The input will always be valid and you do not need to check it explicitly.

Examples:
Input:
5
register John CS1234JS
register George JAVA123S
register Andy AB4142CD
register Jesica VR1223EE
unregister Andy

Output:
John registered CS1234JS successfully
George registered JAVA123S successfully
Andy registered AB4142CD successfully
Jesica registered VR1223EE successfully
Andy unregistered successfully
John => CS1234JS
George => JAVA123S
Jesica => VR1223EE

Input:
4
register Jony AA4132BB
register Jony AA4132BB
register Linda AA9999BB
unregister Jony

Output:
Jony registered AA4132BB successfully
ERROR: already registered with plate number AA4132BB
Linda registered AA9999BB successfully
Jony unregistered successfully
Linda => AA9999BB

Input:
6
register Jacob MM1111XX
register Anthony AB1111XX
unregister Jacob
register Joshua DD1111XX
unregister Lily
register Samantha AA9999BB

Output:
Jacob registered MM1111XX successfully
Anthony registered AB1111XX successfully
Jacob unregistered successfully
Joshua registered DD1111XX successfully
ERROR: user Lily not found
Samantha registered AA9999BB successfully
Joshua => DD1111XX
Anthony => AB1111XX
Samantha => AA9999BB
"""
car_park = {}

for time in range(int(input())):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        reg_number = command[2]
        if username in car_park:
            print(f"ERROR: already registered with plate number {car_park[username]}")
        else:
            car_park[username] = reg_number
            print(f"{username} registered {reg_number} successfully")
    elif command[0] == "unregister":
        if username not in car_park:
            print(f"ERROR: user {username} not found")
        else:
            car_park.pop(username)
            print(f"{username} unregistered successfully")

for username, reg_number in car_park.items():
    print(f"{username} => {reg_number}")
