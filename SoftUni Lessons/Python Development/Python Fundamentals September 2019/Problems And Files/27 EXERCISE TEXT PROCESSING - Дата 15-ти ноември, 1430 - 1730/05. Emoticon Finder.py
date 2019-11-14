"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#4

SUPyF2 Text-Pr.-Ex. - 05. Emoticon Finder

Problem:
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a single symbol or letter.
The input will be provided as a single string.

Examples:
Input:
There are so many emoticons nowadays :P I have many ideas :O what input to place here :)
Output:
:P
:O
:)
"""
text = input()
counter = 0
for i in text:
    if i == ":":
        print(":" + text[counter + 1])
    counter += 1
