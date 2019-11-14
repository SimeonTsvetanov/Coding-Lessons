"""
Programming Fundamentals Mid Exam Retake - 6 August 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1773#2

SUPyF2 P.-Mid-Exam/6 August 2019. - Man O War

Problem:
The pirates encounter a huge Man-O-War at sea.
Create a program that tracks the battle and either chooses a winner or prints a stalemate.
On the first line you will receive the status of the pirate ship,
which is a string representing integer sections separated by '>'.
On the second line you will receive the same type of status, but for the warship:
"{section1}>{section2}>{section3}… {sectionn}"
On the third line you will receive the maximum health capacity a section of the ship can reach.
The following lines represent commands until "Retire":
•	Fire {index} {damage} – the pirate ship attacks the warship with the given damage at that section.
Check if the index is valid and if not skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program:
"You won! The enemy ship has sunken."
•	Defend {startIndex} {endIndex} {damage} - the warship attacks the pirate ship with the given damage at that range
(indexes are inclusive). Check if both indexes are valid and if not skip the command.
If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
•	Repair {index} {health} - the crew repairs a section of the pirate ship with the given health.
Check if the index is valid and if not skip the command.
The health of the section cannot exceed the maximum health capacity.
•	Status – prints the count of all sections of the pirate ship that need repair soon,
which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end if a stalemate occurs print the status of both ships,
which is the sum of their individual sections in the following format:
"Pirate ship status: {pirateShipSum}"
"Warship status: {warshipSum}"
Input
•	On the 1st line you are going to receive the status of the pirate ship (integers separated by '>')
•	On the 2nd line you are going to receive the status of the warship
•	On the 3rd line you are going receive the maximum health a section of a ship can reach.
•	On the next lines, until "Retire", you will be receiving commands.
Output
•	Print the output in the format described above.
Constraints
•	The section numbers will be integers in the range [1….1000]
•	The indexes will be integers [-200….200]
•	The damage will be an integer in the range [1….1000]
•	The health will be an integer in the range [1….1000]
Examples:
Input:
12>13>11>20>66
12>22>33>44>55>32>18
70
Fire 2 11
Fire 8 100
Defend 3 6 11
Defend 0 3 5
Repair 1 33
Status
Retire

Output:
12>13>11>20>66
12>22>33>44>55>32>18
70
Fire 2 11
Fire 8 100
Defend 3 6 11
Defend 0 3 5
Repair 1 33
Status
Retire

Comments:
First, we receive the command "Fire 2 11" and damage the warship at section index 2 which is currently
33 and after reduction the status of the warship is the following:
12 22 22 44 55 32 18
The second and third command have invalid indexes, so we skip them.
The fourth command "Defend 0 3 5" damages 4 sections of the pirate ship with 5 which results in the following status:
7 8 6 15 66
The fifth command "Repair 1 33" repairs the pirate ship section and adds 33 health to the current 8 which results in 41
Only 2 sections of the pirate ship (7 and 6) need repair soon.
In the end there is a stalemate, so we print both ship statuses (sum of all sections).

Input:
2>3>4>5>2
6>7>8>9>10>11
20
Status
Fire 2 3
Defend 0 4 11
Repair 3 18
Retire

Output:
3 sections need repair.
You lost! The pirate ship has sunken.
"""
# ship = [int(section) for section in input().split(">")]
# warship = [int(section) for section in input().split(">")]
# maximum_health_capacity = int(input())
#
# while True:
#     command = input().split()
#     if command[0] == "Retire":
#         break
#
#     elif command[0] == "Fire":
#         index, damage = int(command[1]), int(command[2])
#         if 0 <= index < len(warship):
#             if (warship[index] - damage) <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 exit(0)
#             else:
#                 warship[index] -= damage
#
#     elif command[0] == "Defend":
#         start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
#         if 0 <= start_index < end_index < len(ship):
#             for section in range(start_index, end_index + 1):
#                 if (ship[section] - damage) <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     exit(0)
#                 else:
#                     ship[section] -= damage
#
#     elif command[0] == "Repair":
#         index, health = int(command[1]), int(command[2])
#         if 0 <= index < len(ship):
#             if ship[index] + health >= maximum_health_capacity:
#                 ship[index] = maximum_health_capacity
#             else:
#                 ship[index] += health
#
#     elif command[0] == "Status":
#         sections_for_repair = 0
#         needs_repair = maximum_health_capacity * 0.2
#         for section in ship:
#             if section < needs_repair:
#                 sections_for_repair += 1
#         print(f"{sections_for_repair} sections need repair.")
#
# print(f"Pirate ship status: {sum(ship)}")
# print(f"Warship status: {sum(warship)}")
pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))

max_health = int(input())

lost = False

while True:
    if lost:
        break

    command = input().split()
    if command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif command[0] == "Defend":
        start, end, damage = int(command[1]), int(command[2]), int(command[3])
        if 0 <= start < end < len(pirate_ship):
            for index in range(start, end + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break

    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] >= max_health:
                pirate_ship[index] = max_health

    elif command[0] == "Status":
        minimum_status = max_health * 0.2
        len([x for x in pirate_ship if x < minimum_status])
















































