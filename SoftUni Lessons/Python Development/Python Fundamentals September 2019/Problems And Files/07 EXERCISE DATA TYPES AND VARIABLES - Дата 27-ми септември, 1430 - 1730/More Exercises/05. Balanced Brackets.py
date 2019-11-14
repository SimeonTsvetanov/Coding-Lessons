"""
Data Types and Variables - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1723#4

SUPyF2 D.Types and Vars More Exercises - 05. Balanced Brackets

Problem:
You will receive n lines. On those lines, you will receive one of the following:
•	Opening bracket – “(“,
•	Closing bracket – “)” or
•	Random string
Your task is to find out if the brackets are balanced.
That means after every closing bracket should follow an opening one.
Nested parentheses are not valid, and if two consecutive opening brackets exist,
the expression should be marked as unbalanced.

Input
•	On the first line, you will receive n – the number of lines, which will follow
•	On the next n lines, you will receive “(”, “)” or another string

Output
You have to print “BALANCED”, if the parentheses are balanced and “UNBALANCED” otherwise.

Constraints
•	n will be in the interval [1…20]
•	The length of the stings will be between [1…100] characters

Examples
Input:
8
(
5 + 10
)
* 2 +
(
5
)
-12
Output:
BALANCED

Input:
6
12 *
)
10 + 2 -
(
5 + 10
)

Output:
UNBALANCED
"""
n = int(input())
opened = 0
closed = 0

for i in range(n):
    line = input()
    if line == "(":
        opened += 1
        if (opened - closed) > 1:
            print("UNBALANCED")
            exit(0)
    elif line == ")":
        closed += 1
        if (opened - closed) != 0:
            print("UNBALANCED")
            exit(0)

if opened == closed:
    print("BALANCED")
else:
    print("UNBALANCED")
