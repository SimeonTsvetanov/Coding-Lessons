"""
Data Types and Variables - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1723#3

SUPyF2 D.Types and Vars More Exercises - 04. Decrypting Messages

Problem:
You will receive a key (integer) and n characters afterward.
Add the key to each of the characters and append them to a message.
At the end print the message, which you decrypted.
Input
•	On the first line, you will receive the key
•	On the second line, you will receive n – the number of lines, which will follow
•	On the next n lines – you will receive lower and uppercase characters from the Latin alphabet
Output
Print the decrypted message.
Constraints
•	The key will be in the interval [0…20]
•	n will be in the interval [1…20]
•	The characters will always be upper or lower-case letters from the English alphabet
•	You will receive one letter per line

Examples:
Input:
3
7
P
l
c
q
R
k
f
Output:
SoftUni

Input:
1
7
C
d
b
q
x
o
s
Output:
Decrypt
"""
key = int(input())
n = int(input())
word = ""

for letter in range(n):
    word += chr(ord(input()) + key)

print(word)
