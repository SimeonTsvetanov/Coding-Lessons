"""
Functions - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1728#0

SUPyF2 Functions-Exercise - 01. Smallest of Three Numbers

Problem:
Write a function which receives three integer numbers and returns the smallest.
Use appropriate name for the function.
Examples:
Input:	Output:
2
5
3	    2

600
342
123	    123

25
21
4	    4
"""


# def smallest_integer(all_nums):
#     return min(all_nums)
#
#
# print(smallest_integer([int(input()), int(input()), int(input())]))

a = ["1", "2", "3", "4"]
print(a)
a = list(map(int, a))
a = list(filter(lambda x: x % 2 == 0, a))
print(a)
