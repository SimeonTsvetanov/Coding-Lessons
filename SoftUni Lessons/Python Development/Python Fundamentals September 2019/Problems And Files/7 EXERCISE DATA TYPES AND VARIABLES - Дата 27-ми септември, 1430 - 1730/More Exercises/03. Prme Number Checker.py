"""
Data Types and Variables - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1723#2

SUPyF2 D.Types and Vars More Exercises - 03. Prme Number Checker

Problem:
Write a program to check if a number is prime (only wholly divisible by itself and one).
The input comes as a integer number.
The output should be true for prime number and false otherwise.

Examples:
Input:
7
Output:
True

Input:
8
Output:
False
"""
num = int(input())

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("False")
            break
    else:
        print("True")

else:
    print("False")
