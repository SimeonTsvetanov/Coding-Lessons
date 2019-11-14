"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#7

08. Append Lists

Условие:
Write a program to append several lists of numbers.
- Lists are separated by ‘|’.
- Values are separated by spaces (‘ ’, one or several)
-Order the lists from the last to the first, and their values from left to right.
Examples
Input	                    Output
1 2 3 |4 5 6 |  7  8	    7 8 4 5 6 1 2 3
7 | 4  5|1 0| 2 5 |3	    3 2 5 1 0 4 5 7
1| 4 5 6 7  |  8 9	        8 9 4 5 6 7 1
Hints
- Create a new empty list for the results.
- Split the input by ‘|’ into list of tokens.
- Pass through each of the obtained tokens from tight to left.
- For each token, split it by space and append all non-empty tokens to the results.
- Print the results.
"""

"""
How I solved it:

First we will take all the added strings on one line divided by "|" and it will add them in a new list one by one:
then we need to create a new empty list to store the converted items.
Then using for loop in reverse for each item in the first list. On each cycle of the list we will add the item to
the new(empty) list but we will split the item by " "(blank space).
Then using another list checking each index of the new list. And if the index is NOT empty ("") we will print the index
on one line. Separated by spaces. 
"""

tokens = [str(item) for item in input().split("|")]
nums = []

for item in reversed(tokens):
    nums += item.split(" ")
for num in nums:
    if num != "":
        print(num, end=" ")








