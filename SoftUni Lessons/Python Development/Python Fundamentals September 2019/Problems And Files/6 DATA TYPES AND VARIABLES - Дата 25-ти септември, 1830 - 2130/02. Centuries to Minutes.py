"""
Data Types and Variables - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1721#1
Video: https://www.youtube.com/watch?v=i2vHypjJkB4

SUPyF2 D.Types and Vars Lab - 02. Centuries to Minutes

Problem:
Write program to enter an integer number of centuries and convert it to years, days, hours and minutes.
Input	Output
1	    1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes
5	    5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes

•	Assume that a year has 365.2422 days at average (the Tropical year).
"""
centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = 24 * days
minutes = 60 * hours
print(f"{centuries} = {years} years = {days} days = {hours} hours = {minutes} minutes")
