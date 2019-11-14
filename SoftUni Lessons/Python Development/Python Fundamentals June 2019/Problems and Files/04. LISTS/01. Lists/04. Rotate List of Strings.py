"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#3

04. Rotate List of Strings

Условие:
Write a program to read a list of strings, rotate it to the right and print its rotated items.

Examples:
Input	        Output
a b c d e	    e a b c d
soft uni hi	    hi soft uni
i r a b	        b i r a

Hints:
-You can store the rotated list in a second list alongside the first one
"""

# This will take all the added strings on one line divided by space and it will add them i a new list one by one:
strings = [str(item) for item in input().split(" ")]
# Next. We will create a new list called rotated_strings and its default items are the same as on the strings list.
# But we will use the -1: and :-1 to remove and move the items by 1 to the right.
rotated_strings = strings[-1:] + strings[:-1]
# And finally we will use a For Loop to print each item one by one, and print it on one line with blank space in between
for item in rotated_strings:
    print(item, end=" ")


