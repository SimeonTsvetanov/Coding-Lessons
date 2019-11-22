"""
Regular Expressions - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1742#0

SUPyF2 RegEx-Lab - 01. Match Full Name

Problem:
1.	Match Full Name
Write a program to match full names from a list of names and print them on the console.
Writing the Regular Expression
First, write a regular expression to match a valid full name, according to these conditions:
•	A valid full name has the following characteristics:
o	It consists of two words.
o	Each word starts with a capital letter.
o	After the first letter, it only contains lowercase letters afterwards.
o	Each of the two words should be at least two letters long.
o	The two words are separated by a single space.
To help you out, we've outlined several steps:
1.	Use the online regex tester like https://pythex.org/
2.	Check out how to use character sets (denoted with square brackets - "[]")
3.	Specify that you want two words with a space between them (the space character ' ',
and not any whitespace symbol)
4.	For each word, specify that it should begin with an uppercase letter using a character set.
The desired characters are in a range – from 'A' to 'Z'.
5.	For each word, specify that what follows the first letter are only lowercase letters, one or more –
use another character set and the correct quantifier.
6.	To prevent capturing of letters across new lines, put "\b" at the beginning and at the end of your regex.
This will ensure that what precedes and what follows the match is a word boundary (like a new line).
In order to check your RegEx, use these values for reference (paste all of them in the Test String field):

Match ALL of these	            Match NONE of these
Ivan Ivanov	                    ivan ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Ivan IvAnov, Ivan Ivanov

We should extract all the names from the first part from the second:
After you've constructed your regular expression, it's time to write the solution.

Implementing the Solution
Import re, create your pattern (don't forget to escape the special characters) and use the findall()
method to get all the matches. Then print them
"""

# this initial Solution
"""
import re
names = input()
matches = re.findall(r"\b([A-Z][a-z]+ [A-Z][a-z]+)", names)
print(" ".join(matches))
"""
# From work at class:

import re

pattern = r"\b[A-Z][a-z]+[ ][A-Z][a-z]+\b"
text = input()
matches = re.findall(pattern, text)
print(" ".join(matches))

