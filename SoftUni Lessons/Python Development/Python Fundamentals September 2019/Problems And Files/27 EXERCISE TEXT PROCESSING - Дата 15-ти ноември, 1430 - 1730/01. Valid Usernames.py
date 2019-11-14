"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#0

SUPyF2 Text-Pr.-Ex. - 01. Valid Usernames

Problem:
Write a program that reads user names on a single line (joined by ", ") and prints all valid usernames.
A valid username is:
•	Has length between 3 and 16 characters
•	Contains only letters, numbers, hyphens and underscores
•	Has no redundant symbols before, after or in between

Examples:
-----------------------------------------------------------------------------

Input:                                                          Output:
sh, too_long_username, !lleg@l ch@rs, jeffbutt	                jeffbutt
-----------------------------------------------------------------------------
Input:                                                          Output:
Jeff, john45, ab, cd, peter-ivanov, @smith	                    Jeff
                                                                John45
                                                                peter-ivanov
-----------------------------------------------------------------------------
"""
all_names = input().split(", ")
valid_names = []
for name in all_names:
    if 3 <= len(name) <= 16:
        all_valid = True
        valid_name = ""
        for letter in name:
            if letter.isalpha() or letter.isdigit() or letter == "-" or letter == "_":
                valid_name += letter
            else:
                all_valid = False
        if all_valid:
            valid_names += [valid_name]
print("\n".join(valid_names))

