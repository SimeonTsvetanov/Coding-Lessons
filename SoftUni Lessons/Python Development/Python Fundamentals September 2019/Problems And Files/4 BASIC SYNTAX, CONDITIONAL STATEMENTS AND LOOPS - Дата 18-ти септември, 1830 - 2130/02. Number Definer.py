"""
Basic Syntax, Conditional Statements and Loops - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1718#1
Video: https://www.youtube.com/watch?v=sP_t7cbZF7c

SUPyF2 Basic - 02. Number Definer

Problem:
Write a program that reads a floating-point number and prints "zero" if the number is zero.
Otherwise, print "positive" or "negative". Add "small" if the absolute value of the number is less than 1,
or "large" if it exceeds 1 000 000.
Example:

Input:              |Output:
------------------------------------
25	                |positive
0.7                 |small positive
435247392.921	    |large positive
-0.005	            |small negative
-103.21	            |negative
-358583355123.001   |large negative
"""
num = float(input())

if num == 0:
    print("zero")
elif num > 0:
    if num < 1:
        print("small positive")
    elif num > 1000000:
        print("large positive")
    else:
        print("positive")
elif num < 0:
    if abs(num) < 1:
        print("small negative")
    elif abs(num) > 1000000:
        print("large negative")
    else:
        print("negative")
