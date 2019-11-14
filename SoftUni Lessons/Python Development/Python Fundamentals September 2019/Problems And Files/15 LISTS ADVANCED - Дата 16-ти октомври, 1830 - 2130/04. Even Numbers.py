"""
Lists Advanced - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1730#3

SUPyF2 Lists-Advanced-Lab - 04. Even Numbers

Problem:
Write a program that reads a single string with numbers separated by comma and space ", ".
Print the indices of all even numbers

Example:
Input:	            Output:
3, 2, 1, 5, 8	    [1, 4]
2, 4, 6, 9, 10	    [0, 1, 2, 4]

Hints:
Read the string, split it and convert the list of strings into a list of numbers using lambda.
"""
numbers = [int(number) for number in input().split(", ")]
print([numbers.index(number) for number in numbers if number % 2 == 0])

