"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1720#1
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise More - 02. Find The Capitals

Problem:
Write a program that takes a single string and prints a list of all the indices of all the capital letters

Examples:
Input:	    Output:
pYtHoN	    [1, 3, 5]
CApiTAls	[0, 1, 4, 5]

Hint:
If you don't know what lists are, search them in google, find out how to create them and add elements to them
"""
# text = [letter for letter in input()]
# list_capitals = []
#
# for letter in range(len(text)):
#     if text[letter].isupper():
#         list_capitals += [letter]
#
# print(list_capitals)

# input_string = input()

input_string = input()
n = [i for i in range(len(input_string)) if input_string[i].isupper()]
print(n)

