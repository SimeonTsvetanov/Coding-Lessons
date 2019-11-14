"""
Programming Fundamentals Mid Exam - 2 November 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/1862/Programming-Fundamentals-Mid-Exam-2-November-2019-Group-2

SUPyF2 P.-Mid-Exam/2 November 2019/2. - Experience Gaining

Problem:
Tom is a world of tanks player and he likes to collect premium tanks.
You will receive a list of Tom's already owned premium vehicles on a single line separated by ", ".
On the next n lines you will receive commands that could be:
•	Add, {tankName}: Check if he already owns the wanted tank.
•	If he owns it, print on console:  "Tank is already bought"
•	If not, print on console:  "Tank successfully bought" and add it to the tank list.
•	Remove, {tankName}: Check if he owns the tank.
•	If he owns it print on console:  "Tank successfully sold" and remove it from the tank list.
•	If not print on console: "Tank not found"
•	Remove At, {index}: Check if the index is in the range of the list.
•	If not print on console: "Index out of range" and continue.
•	If it’s in range, remove at the given index and print on console: "Tank successfully sold"
•	Insert, {index}, {tankName}: Check if the index is in range of the list and check if he already owns the tank.
•	If not print on console: "Index out of range" and continue.
•	If it's in range and he doesn't own the tank then add the tank at the given index and print on console:
•	"Tank successfully bought"
•	If the tank is in range and he owns it already than print on console:
•	"Tank is already bought"
After you go through all the commands you need to print the list on a single line separated by ", ".

Input:
•	The first input line will contain the list of already owned tanks.
•	The second input line  will be  the number of commands – an integer number in range [0…50].
•	On the next input lines you will be receiving commands.

Output:
•	As output you must print a single line containing the elements of the list, joined by  ", ".

Examples:

Input:
T-34-85 Rudy, SU-100Y, STG
3
Add, King Tiger(C)
Insert, 2, IS-2M
Remove, T-34-85 Rudy

Output:
Tank successfully bought
Tank successfully bought
Tank successfully sold
SU-100Y, IS-2M, STG, King Tiger(C)

Comments:
The first command gives the tank list so its splitted and added into the list.
"T-34-85 Rudy, SU-100Y, STG"
The second commands gives the number of commands that will be received.
"3"
The Add command adds the tank to the list after the necessary checks.
"Add, King Tiger(C)" – "Tank successfully bought"
The Insert commands also adds the tank at the given spot after the necessary checks.
"Insert, 2, IS-2M" – "Tank successfully bought"
The Remove command is the last one and after the checks the tank is sold.
"Remove, T-34-85 Rudy" – "Tank successfully sold"
After that we print the list on the console.
"SU-100Y, IS-2M, STG, King Tiger(C)"

Input:
T 34, T 34 B, T92, AMX 13 57
4
Add, T 34
Remove, AMX CDC
Insert, 10, M60
Remove At, 1

Output:
Tank is already bought
Tank not found
Index out of range
Tank successfully sold
T 34, T92, AMX 13 57
"""
owned_tanks = input().split(", ")
num = int(input())

for i in range(num):
    command = input().split(", ")

    if command[0] == "Add":
        tank_name = command[1]
        if tank_name in owned_tanks:
            print(f"Tank is already bought")
        else:
            owned_tanks.append(tank_name)
            print("Tank successfully bought")

    elif command[0] == "Remove":
        tank_name = command[1]
        if tank_name in owned_tanks:
            owned_tanks.remove(tank_name)
            print("Tank successfully sold")
        else:
            print("Tank not found")

    elif command[0] == "Remove At":
        index = int(command[1])
        if 0 <= index < len(owned_tanks):
            owned_tanks.pop(index)
            print(f"Tank successfully sold")
        else:
            print(f"Index out of range")

    elif command[0] == "Insert":
        index, tank_name = int(command[1]), command[2]
        if 0 <= index < len(owned_tanks):
            if tank_name not in owned_tanks:
                owned_tanks.insert(index, tank_name)
                print(f"Tank successfully bought")
            else:
                print("Tank is already bought")
        else:
            print(f"Index out of range")

print(', '.join(owned_tanks))
