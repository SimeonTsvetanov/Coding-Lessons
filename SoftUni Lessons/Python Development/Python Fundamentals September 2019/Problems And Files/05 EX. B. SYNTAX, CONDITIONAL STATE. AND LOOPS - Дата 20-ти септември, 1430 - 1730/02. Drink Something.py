"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#1
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 02. Drink Something

Problem:
Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
Make a program that receives an age, and returns what they drink.
Rules:
Kids under 14 years old.
Teens under 18 years old.
Young adults under 21 years old.
Adults above 21.
Note: All the values except the last one are inclusive!

Examples:
Input:	Output:
13	    drink toddy
17	    drink coke
21	    drink beer
30	    drink whisky
"""

age = int(input())

if age <= 14:
    print("drink toddy")
elif 14 < age <= 18:
    print("drink coke")
elif 18 < age <= 21:
    print("drink beer")
else:
    print("drink whisky")

