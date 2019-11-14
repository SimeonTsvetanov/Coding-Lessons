"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1511#0

SUPyF Exam 10.03.2019 - 01. Listmons delivery problem

Problem:
Listmon is a delivery guy. He should deliver a barrels with a mystic liquid.
He has got a truck but he is not good at math so he asks you to help him.
You have a task to estimate how many barrels can be transported with the single truck.
The shape is rectangular parallelepiped and the barrel's shape always will be circular cylinder.
If at some point the truck get full, you should stop receiving  barrels data and print
„Truck is full.{count_of_barrels} on board!“.
Where the count_of_barrels are the barrels you have succesfuly loaded up.
If you have succesfully loaded up all barrels without breaking up the program you should print –
„All barrels on board.Capacity left - {volume_of_truck}.“
where the volume_of_truck is the free volume space has left.
Where the volume is formatetd up to 2 digit after decimal point.
Input
You will recieve on the first 3 lines:
•	a – width of the truck [floating  number]
•	b – depth of the truck [floating number]
•	c – height of the truck [floating number]
On the next line you will recieve
•	n - number of barrels [integer number]
For each barrel tou will receive:
•	r - radius of the barrel [floating  number]
•	h -  height of the barrel [floating  number]

Output
If you have loaded up all barrels you should print
•	"All barrels on board. Capacity left - {volume_of_truck}."
Formatted two digits after decimal point.
If you have no space left in the truck you should print
•	"Truck is full. {count_of_barrels} on board!"

Examples:
Input:
300
150
200
6
100
100
100
100
100
100
100
100
100
100
100
100
Output:
Truck is full. 2 on board!
Input:
100
100
50
2
20
40
30
60
Output:
All barrels on board. Capacity left - 280088.51.
"""

import math

a = float(input())
b = float(input())
c = float(input())

n = int(input())

truck_volume = a * b * c
count_barrels_on_board = 0

no_more_space = False

for barrel in range(1, n + 1):
    r = float(input())
    h = float(input())
    v = math.pi * r * r * h
    if truck_volume > v:
        count_barrels_on_board += 1
        truck_volume -= v
    else:
        no_more_space = True
        break

if no_more_space:
    print(f"Truck is full. {count_barrels_on_board} on board!")
else:
    print(f"All barrels on board. Capacity left - {truck_volume:.2f}.")
