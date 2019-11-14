"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#1

SUPyF2 Lists-Advanced-Exercise - 02. Big Numbers Lover

Problem:
You really like big numbers, so you always find a way to form one from numbers given to you
You will receive a single line containing numbers separated by a single space.
Form the biggest number possible from them.

Example:
Input:             Output:              Comments:
3 30 34 5 9	       9534303	            The numbers sorted are 9 5 34 30 3
1 2 3	           321
"""

numbers = [number for number in input().split()]
numbers = sorted(numbers, reverse=True)
print("".join(numbers))




