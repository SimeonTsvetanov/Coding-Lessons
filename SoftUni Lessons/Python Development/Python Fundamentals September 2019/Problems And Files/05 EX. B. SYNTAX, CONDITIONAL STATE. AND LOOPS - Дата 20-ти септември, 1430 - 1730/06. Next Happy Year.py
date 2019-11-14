"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#5
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 06. Next Happy Year

Problem:
You're saying good-bye your best friend, "See you next happy year". Happy Year is the year with only distinct digits,
(e.g) 2018. Write a program that receives an integer number and finds the next happy year.

Examples:
Input	Output
8989	9012
1001	1023

"""
year = int(input()) + 1

while True:
    if len(set(str(year))) == len(str(year)):
        print(year)
        break
    else:
        year += 1
