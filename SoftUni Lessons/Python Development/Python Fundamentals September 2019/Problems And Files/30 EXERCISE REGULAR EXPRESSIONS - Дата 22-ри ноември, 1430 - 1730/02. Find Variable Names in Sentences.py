"""
Regular Expressions - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1743#1

Name: 02. Find Variable Names in Sentences

Problem:
Write a program that finds all variable names in a given string. A variable name starts with an underscore ("_")
and contains only Capital and Non-Capital English Alphabet letters and digits.
Extract only their names, without the underscore. Try to do this only with regular expressions.
The output consists of all variable names, extracted and printed on a single line, each separated by a comma.

Examples:
Input:
The _id and _age variables are both integers.
Output:
id,age

Input:
Calculate the _area of the _perfectRectangle object.
Output:
area,perfectRectangle

Input:
__invalidVariable _evenMoreInvalidVariable_ _validVariable
Output:
validVariable
"""
import re
pattern = r"\b_[a-zA-Z0-9]+\b"
text = input()
matches = [x[1:]for x in re.findall(pattern, text)]
print(",".join(matches))
