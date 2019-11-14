"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#4

SUPyF2 Functions-Exercise - 05. Palindrome Integers

Problem:
A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
Write a function which receives a list of positive integers and checks if each integer is a palindrome or not.
Print the results on the console
The input will be a single string containing the numbers separated by comma and space ", "

Examples:
Input:
123, 323, 421, 121

Output:
False
True
False
True

Input:
32, 2, 232, 1010

Output:
False
True
True
False

Hints:
•	Read more about palindromes: https://en.wikipedia.org/wiki/Palindrome

"""


def palindrome(string):
    for each_string in [word for word in string.split(", ")]:
        if each_string == each_string[::-1]:
            print("True")
        else:
            print("False")


palindrome(input())

