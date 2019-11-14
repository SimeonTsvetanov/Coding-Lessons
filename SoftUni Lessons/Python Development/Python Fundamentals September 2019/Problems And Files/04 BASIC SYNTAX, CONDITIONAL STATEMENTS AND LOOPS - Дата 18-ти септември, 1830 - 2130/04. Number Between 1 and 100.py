"""
Basic Syntax, Conditional Statements and Loops - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1718#3
Video: https://www.youtube.com/watch?v=sP_t7cbZF7c

SUPyF2 Basic - 04. Number Between 1 and 100

Problem:
Write a program which reads numbers from the console until it receives a number between 1 and 100 inclusive.
When the correct number is received, stop reading and print "The number {number} is between 1 and 100"

Examples:

    Input:
-3
0.9
44

    Output:
The number 44.0 is between 1 and 100
"""
number = float(input())

while True:
    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100")
        break
    else:
        number = float(input())

