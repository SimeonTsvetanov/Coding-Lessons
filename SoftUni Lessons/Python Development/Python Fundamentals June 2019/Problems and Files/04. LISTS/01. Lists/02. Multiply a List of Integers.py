"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#1

02. Multiply a List of Integers

Условие:
Write a program to read a list of ints, a int p, multiply each item by p and print the resulting list.

Hints
-Read the list
-Loop through the list, multiplying each item by p
-Finally, print the resulting list, using a for loop
"""

nums = [int(item) for item in input().split(" ")]
multiply_by = int(input())

for item in nums:
    print(f"{(item * multiply_by)}", end=" ")


