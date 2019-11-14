"""
Text Processing - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1741#1

SUPyF2 Text-Pr.-More-Ex. - 02. Ascii Sumator

Problem:
Write a program that prints a sum of all characters between two given characters (their ascii code).
On the first line you will get a character. On the second line you get another character.
On the last line you get a random string. Find all the characters between the two given and print their ascii sum.

Examples:
Input:
.
@
dsg12gr5653feee5

Output:
363

Input:
?
E
@ABCEF

Output:
262
"""
a = ord(input())
b = ord(input())
text = [ord(x) for x in input()]
start = min(a, b)
end = max(a, b)
total = 0
for i in text:
    if start < i < end:
        total += i
print(total)
