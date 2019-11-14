"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#6
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 07. Maximum Multiple

Problem:
Given a Divisor and a Bound, find the largest integer N, such that:
N is divisible by divisor
N is less than or equal to bound
N is greater than 0.

Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found

Examples:
Input:	Output:
2
7	    6

10
50	    50

37
200	    185
"""

divisor = int(input())
bound = int(input())
number = bound

while True:
    if number % divisor == 0:
        print(number)
        break
    else:
        number -= 1
