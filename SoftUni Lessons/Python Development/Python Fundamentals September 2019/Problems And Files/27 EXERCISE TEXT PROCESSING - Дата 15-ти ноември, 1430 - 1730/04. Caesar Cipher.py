"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#3

SUPyF2 Text-Pr.-Ex. - 04. Caesar Cipher

Problem:
Write a program that returns an encrypted version of the same text.
Encrypt the text by shifting each character with three positions forward.
For example A would be replaced by D, B would become E, and so on. Print the encrypted text.

Examples
Input	                Output
Programming is cool!	Surjudpplqj#lv#frro$
One year has 365 days.	Rqh#|hdu#kdv#698#gd|v1
"""

# The coolest way to sole this solution is:
# print(''.join(chr(ord(letter) + 3) for letter in input()))

# The longer option from work at class:

text = input()
result = [chr((ord(x) + 3)) for x in text]
print(''.join(result))



