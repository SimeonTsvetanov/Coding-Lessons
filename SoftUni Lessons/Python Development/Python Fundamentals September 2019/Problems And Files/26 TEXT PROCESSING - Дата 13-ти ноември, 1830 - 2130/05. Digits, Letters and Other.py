"""
Text Processing - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1739#4

SUPyF2 Text-Processing-Lab - 05. Digits, Letters and Other

Problem:
Write a program that receives a single string and on the first line prints all the digits,
on the second – all the letters, and on the third – all the other characters.
There will always be at least one digit, one letter and one other characters.
Examples
Input	            Output
Agd#53Dfg^&4F53 	53453
                    AgdDfgF
                    #^&
"""
string = input()
print(''.join([letter for letter in string if letter.isdigit()]))
print(''.join([letter for letter in string if letter.isalpha()]))
print(''.join([letter for letter in string if not letter.isdigit() and not letter.isalpha()]))
