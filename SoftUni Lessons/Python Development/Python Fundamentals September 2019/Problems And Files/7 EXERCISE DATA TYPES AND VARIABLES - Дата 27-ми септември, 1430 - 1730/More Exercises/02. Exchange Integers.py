"""
Data Types and Variables - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1723#1

SUPyF2 D.Types and Vars More Exercises - 02. Exchange Integers

Problem:
Read two integer numbers and after that exchange their values by using some programming logic.
Print the variable values before and after the exchange, as shown below:

Examples:
Input
5
10
Output:
Before:
a = 5
b = 10
After:
a = 10
b = 5
You may use a temporary variable to remember the old value of a, then assign the value of b to a,
then assign the value of the temporary variable to b.
"""
a = int(input())
b = int(input())
print(f"Before:\na = {a}\nb = {b}")
c = a
a = b
b = c
print(f"After:\na = {a}\nb = {b}")

