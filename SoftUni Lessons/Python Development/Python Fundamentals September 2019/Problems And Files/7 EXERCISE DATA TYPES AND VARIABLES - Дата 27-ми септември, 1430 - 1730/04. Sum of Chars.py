"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#3

SUPyF2 D.Types and Vars Exercise - 04. Sum of Chars
Problem:
Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
Input
•	On the first line, you will receive n – the number of lines, which will follow
•	On the next n lines – you will receive letters from the Latin alphabet
Output
Print the total sum in the following format:
The sum equals: {total_sum}
Constraints
•	n will be in the interval [1…20].
•	The characters will always be either upper or lower-case letters from the English alphabet
•	You will always receive one letter per line
Examples:
Input:
5
A
b
C
d
E
Output:
The sum equals: 399
Input:
12
S
o
f
t
U
n
i
R
u
l
z
z
Output:
The sum equals: 1263
"""
total = 0
for symbol in range(int(input())):
    total += ord(input())

print(f"The sum equals: {total}")
