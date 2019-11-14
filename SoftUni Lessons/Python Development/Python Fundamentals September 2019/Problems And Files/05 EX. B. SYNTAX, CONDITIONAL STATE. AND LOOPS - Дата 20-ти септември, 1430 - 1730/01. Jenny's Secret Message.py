"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#0
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 01. Jenny's Secret Message

Problem:
Jenny studies programming with python and wants to create a program that greets a user when he/she gives his/her name.
Jenny however is in love with Johnny, and would like to greet him differently. Can you help her?
Examples:

    Input:
Peter
    Output:
Hello, Peter!

    Input:
Amy
    Output:
Hello, Amy!

    Input:
Johnny
    Output:
Hello, my love!
"""

name = input()

if name == "Johnny":
    name = "my love"

print(f"Hello, {name}!")
