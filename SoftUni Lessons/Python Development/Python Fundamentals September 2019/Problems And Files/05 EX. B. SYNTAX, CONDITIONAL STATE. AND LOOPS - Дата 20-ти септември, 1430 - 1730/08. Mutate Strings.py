"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#7
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 08. Mutate Strings (not included in final score)

Problem:
You will be given two strings. Transform the first string into the second one, one letter at a time and print it.
Print only the unique strings
Note: the strings will have the same lengths

Examples:
Input:
bubble gum
turtle hum
Output:
tubble gum
turble gum
turtle gum
turtle hum
turtle ham
Input:
Kitty
Doggy
Output:
Ditty
Dotty
Dogty
Doggy
"""

string_1 = [letter for letter in input()]
string_2 = [letter for letter in input()]

for letter in range(len(string_2)):
    if string_1[letter] != string_2[letter]:
        string_1[letter] = string_2[letter]
        print("".join(string_1))

