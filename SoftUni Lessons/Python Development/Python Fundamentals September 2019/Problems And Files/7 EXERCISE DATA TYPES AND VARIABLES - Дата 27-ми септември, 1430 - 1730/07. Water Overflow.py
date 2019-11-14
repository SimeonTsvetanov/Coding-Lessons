"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#6

SUPyF2 D.Types and Vars Exercise - 07. Water Overflow
Problem:
You have a water tank with capacity of 255 liters.
On the next n lines, you will receive liters of water, which you have to pour in your tank.
If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line,
print the liters in the tank.
Input
The input will be on two lines:
•	On the first line, you will receive n – the number of lines, which will follow
•	On the next n lines – you receive quantities of water, which you have to pour in the tank
Output
Every time you do not have enough capacity in the tank to pour the given liters, print:
Insufficient capacity!
On the last line, print only the liters in the tank.
Constraints
•	n will be in the interval [1…20]
•	liters will be in the interval [1…1000]
Examples:
INPUT:
5
20
100
100
100
20
OUTPUT:
Insufficient capacity!
240

INPUT:
1
1000
OUTPUT:
Insufficient capacity!
0
"""
capacity = 0
for each_time in range(int(input())):
    liters = int(input())
    if capacity + liters > 255:
        print("Insufficient capacity!")
    else:
        capacity += liters
print(capacity)
