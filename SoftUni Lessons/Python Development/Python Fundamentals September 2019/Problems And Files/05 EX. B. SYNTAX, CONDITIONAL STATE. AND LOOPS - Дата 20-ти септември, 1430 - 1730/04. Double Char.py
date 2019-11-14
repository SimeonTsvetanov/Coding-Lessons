"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#3
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 04. Double Char

Problem:
Given a string, you have to print a string in which each character (case-sensitive) is repeated once.

Examples:
Input	        Output
Hello World	    HHeelllloo  WWoorrlldd
1234!	        11223344!!
"""

word = input()
new_word = ""

for letter in word:
    new_word += letter * 2

print(new_word)
