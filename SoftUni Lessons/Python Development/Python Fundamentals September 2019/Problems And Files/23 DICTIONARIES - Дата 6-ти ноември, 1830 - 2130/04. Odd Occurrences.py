"""
Dictionaries - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1736#3

SUPyF2 Dictionaries-Lab - 04. Odd Occurrences

Problem:
Write a program that extracts all elements from a given sequence of words that are present
in it an odd number of times (case-insensitive).
•	Words are given on a single line, space separated.
•	Print the result elements in lowercase, in their order of appearance.

Examples:
Input	                                Output
Java C# PHP PHP JAVA C java	            java c# c
3 5 5 hi pi HO Hi 5 ho 3 hi pi	        5 hi
a a A SQL xx a xx a A a XX c	        a sql xx c
"""

words = [word.lower() for word in input().split()]
print(*{word: words.count(word) for word in words if words.count(word) % 2 != 0}.keys())
