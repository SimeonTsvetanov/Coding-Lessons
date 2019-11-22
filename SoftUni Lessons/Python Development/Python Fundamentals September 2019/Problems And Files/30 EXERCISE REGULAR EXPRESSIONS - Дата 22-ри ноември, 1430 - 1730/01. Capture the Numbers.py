"""
Regular Expressions - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1743#0

Name: 01. Capture the Numbers

Problem:
Write a program that finds all numbers in a sequence of strings.
The output is all the numbers, extracted and printed on a single line – each separated by a single space.

Examples:

Input:
The300
What is that?
I think it's the 3rd movie
Lets watch it at 22:45

Output:
300 3 22 45

Input:
123a456
789b987
654c321
0

Output:
123 456 789 987 654 321 0

Input:
Let's go11!!!11!
Okey!1!

Output:
11 11 1
"""
import re

pattern = r"\d+"

while True:
    line = input()
    if not line:
        break

    matches = re.findall(pattern, line)
    for match in matches:
        print(match, end=" ")
