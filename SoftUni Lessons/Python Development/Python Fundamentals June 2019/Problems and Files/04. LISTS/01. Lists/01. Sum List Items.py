"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#0

01. Sum List Items

Условие:
Write a program, which reads a list of integers, calculates its sum and prints it.
The input consists of a number n (the number of items) + n integers, each as a separate line.
Examples:

Input:
4
1
2
3
4
Output:	10

Input:
5
1
1
1
1
1
Output: 5
Input:
4
2
-1
-2
8
Output: 7
Hints
-First, read the number n.
-Read the integers in a for-loop.
"""

# Цялата задача на един ред:
# print(sum([int(input()) for entry in range(int(input()))]))

n = int(input())

list_1 = []

for entry in range(n):
    list_1 += [int(input())]

print(sum(list_1))

nums = [int(input()) for entry in range(n)]

# """
# Write a program, which reads a list of integers, calculates its sum and prints it.
# The input consists of a number n (the number of items) + n integers, each as a separate line.
# """
# 
# print(sum([int(input()) for each_time in range(int(input()))]))
