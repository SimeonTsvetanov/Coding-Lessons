"""
Data Types and Variables - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1721#3
Video: https://www.youtube.com/watch?v=i2vHypjJkB4

SUPyF2 D.Types and Vars Lab - 04. Convert Meters to Centimeters

Problem:
You will be given an integer that will be distance in meters.
Write a program that converts meters to kilometers formatted to the second decimal point.

Examples:
Input:	Output:
1852	1.85
798	    0.80
"""
print(f"{(int(input()) / 1000):.2f}")
