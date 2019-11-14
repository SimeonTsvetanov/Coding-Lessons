"""
Basic Syntax, Conditional Statements and Loops - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1718#4
Video: https://www.youtube.com/watch?v=sP_t7cbZF7c

SUPyF2 Basic - 05. Patterns

Problem:
Write a program to create the following pattern:
*
**
***
**
*
You will receive a number that represents the highest number of stars.

Examples:

    Input:
3
    Output:
*
**
***
**
*

Input:
5
Output:
*
**
***
****
*****
****
***
**
*
"""
stars = int(input())

for star in range(1, stars + 1):
    for second_star in range(0, star):
        print("*", end="")
    print()
for star in range(stars - 1, 0, -1):
    for second_star in range(0, star):
        print("*", end="")
    print()
