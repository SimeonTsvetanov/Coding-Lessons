"""
Functions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1727#0

SUPyF2 Functions-Lab - 01. Grades

Problem:
1.	Grades
Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words
•	2.00 – 2.99 - "Fail"
•	3.00 – 3.49 - "Poor"
•	3.50 – 4.49 - "Good"
•	4.50 – 5.49 - "Very Good"
•	5.50 – 6.00 - "Excellent"

Examples:
Input:	Output:
3.33	Poor
4.50	Very Good
2.99	Fail
"""


def grades(score):
    if 2.00 <= score <= 2.99:
        return "Fail"
    elif 3.00 <= score <= 3.49:
        return "Poor"
    elif 3.50 <= score <= 4.49:
        return "Good"
    elif 4.50 <= score <= 5.49:
        return "Very Good"
    elif 5.50 <= score <= 6.00:
        return "Excellent"


print(grades(float(input())))
