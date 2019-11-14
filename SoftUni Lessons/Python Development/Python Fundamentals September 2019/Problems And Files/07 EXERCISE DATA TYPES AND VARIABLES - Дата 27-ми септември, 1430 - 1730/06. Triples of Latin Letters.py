"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#5

SUPyF2 D.Types and Vars Exercise - 06. Triples of Latin Letters
Problem:
Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:
Examples:
Input:
3
Output:
aaa
aab
aac
aba
abb
abc
aca
acb
acc
baa
bab
bac
bba
bbb
bbc
bca
bcb
bcc
caa
cab
cac
cba
cbb
cbc
cca
ccb
ccc
"""
num = int(input())
for a in range(num):
    for b in range(num):
        for c in range(num):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}")
