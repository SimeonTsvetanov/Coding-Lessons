"""
Technology Fundamentals Mid Exam - 10 March 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1555#1

SUPyF2 P.-Mid-Exam/10 March 2019/2 - 02. Seize the Fire

Problem:
The group of adventurists have gone on their first task. Now they have to walk through fire - literally.
They have to use all of the water they have left. Your task is to help them survive.
Create a program that calculates the water that is needed to put out a "fire cell",
based on the given information about its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell,
which represents the needed water to put out the fire.  They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
Afterwards you will receive the amount of water you have for putting out the fires.
There is a range of fire for each of the fire types,
and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.
Type of Fire	Range
High	81 - 125
Medium	51 - 80
Low	1 - 50
If a cell is valid, you have to put it out by reducing the water with its value.
Putting out fire also takes effort and you need to calculate it.
Its value is equal to 25% of the cell’s value. In the end you will have to print the total effort.
Keep putting out cells until you run out of water.
If you don’t have enough water to put out a given cell – skip it and try the next one.
In the end, print the cells you have put out in the following format:
"Cells:
 - {cell1}
 - {cell2}
 - {cell3}
……
 - {cellN}"
"Effort: {effort}"
In the end, print the total fire you have put out from all of the cells in the following format:
    "Total Fire: {totalFire}"
Input / Constraints
•	On the 1st line you are going to receive the fires with their cells in the format described above –
integer numbers in the range [1…500]
•	On the 2nd line, you are going to be given the water – an integer number in the range [0….100000]
Output
•	Print the cells, which you have put out in the following format:
"Cells:
 - {cell}
 - {cell2}
 - {cell3}
 - {cell5}
……
 - {cellN}"
•	Print the effort, rounded 2 digits after the decimal separator in the following format:
"Effort: {effort}"
•	Print the total fire put out
"Total Fire: {totalFire}"

Examples:
Input:
High = 89#Low = 28#Medium = 77#Low = 23
1250

Output:
High = 89#Low = 28#Medium = 77#Low = 23
1250

Comments:
After reading the output, we start checking the level of the fire and its validity.
The first is valid, so we subtract the 89 from the amount of water – 1250, and the water becomes 1161.
We need to calculate the effort, which is 25% of 89. We will add 89 to the total fire we have put out.
In the end the effort is 54.22 and the total fire: 217

Input:
High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
220

Output:
Cells:
 - 40
 - 110
Effort: 37.50
Total Fire: 150
"""
all_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
valid_cells = []

for cell in all_cells:
    value_of_cell, type_of_fire = cell.split(" = ")
    type_of_fire = int(type_of_fire)
    if (value_of_cell == "High" and (81 <= type_of_fire <= 125)) or \
            (value_of_cell == "Medium" and (51 <= type_of_fire <= 80)) or \
            (value_of_cell == "Low" and (1 <= type_of_fire <= 50)):
        if water - type_of_fire >= 0:
            water -= type_of_fire
            effort += type_of_fire * 0.25
            total_fire += type_of_fire
            valid_cells += [type_of_fire]

print(f"Cells:")
for cell in valid_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
