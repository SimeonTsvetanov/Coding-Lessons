"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#2

SUPyF2 Functions-Exercise - 03. Characters in Range

Problem:
Write a function that receives two characters and returns a single string with all the
characters in between them according to the ASCII code.
Examples:
Input:	    Output:
a
d	        b c

#
:	        $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9

C
#	        $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
"""


def char_in_range(char_1, char_2):
    all_characters = []
    for character in range((ord(char_1) + 1), ord(char_2)):
        all_characters += [chr(character)]
    return " ".join(all_characters)


print(char_in_range(input(), input()))

