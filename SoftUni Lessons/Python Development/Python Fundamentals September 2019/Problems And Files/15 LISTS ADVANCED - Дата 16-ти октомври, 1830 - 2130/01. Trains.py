"""
Lists Advanced - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1730#0

SUPyF2 Lists-Advanced-Lab - 01. Trains

Problem:
You will receive how many wagons the train has. Create a list with that length with all zeros.
Until you receive the command "End", you get some of the following commands:
•	add {people} -> adds the people in the last wagon
•	insert {index} {people} -> adds the people at the given wagon
•	leave {index} {people} -> removes the people from the wagon
After you receive the "End" command print the train

Example:

Input:	        Output:
3               [10, 0, 20]
add 20
insert 0 15
leave 0 5
End

5               [16, 32, 100, 0, 105]
add 10
add 20
insert 0 16
insert 1 44
leave 1 12
insert 2 100
insert 4 61
leave 4 1
add 15
End
"""
wagons_count = int(input())
wagons_list = [0] * wagons_count

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "add":
        wagons_list[-1] += int(command[1])
    elif command[0] == "insert":
        wagons_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        wagons_list[int(command[1])] -= int(command[2])

print(wagons_list)



