"""
Text Processing - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1739#2

SUPyF2 Text-Processing-Lab - 03. Substring

Problem:
On the first line you will receive a string. On the second line you will receive a second string.
Write a program that removes all of the occurrences of the first string in the second until there is no match.
At the end print the remaining string.

Example:
Input:	Output:
ice     kicegiciceeb

Comment:
kgb	We remove ice once and we get "kgiciceeb"
We match "ice" one more time and we get "kgiceb"
There is one more match. The finam result is "kgb"
"""
to_remove = input()
string = input()

while to_remove in string:
    string = string.replace(to_remove, '')
print(string)
