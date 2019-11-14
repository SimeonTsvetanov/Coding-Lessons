"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/423#2

03. Sum Adjacent Equal Numbers

Условие:
Write a program to sum all adjacent equal numbers in a list of decimal numbers, starting from left to right.
- After two numbers are summed, the obtained result could be equal to some of its neighbors and should be
summed as well (see the examples below).
- Always sum the leftmost two equal neighbors (if several couples of equal neighbors are available).
Examples
Input	        Output	    Explanation
3 3 6 1	        12 1	    3 3 6 1  6 6 1  12 1
8 2 2 4 8 16	16 8 16	    8 2 2 4 8 16      8 4 4 8 16  8 8 8 16  16 8 16
5 4 2 1 1 4	    5 8 4	    5 4 2 1 1 4  5 4 2 2 4  5 4 4 4  5 8 4

Hints
1.	Read the input and parse it to list of numbers.
2.	Find the leftmost two adjacent equal cells.
3.	Replace them with their sum.
4.	Repeat (1) and (2) until no two equal adjacent cells survive.
5.	Print the processed list of numbers.
"""

nums = [float(item) for item in input().split(" ")]

i = 0
while i != len(nums):
    if len(nums) == 1:
        break
    f = nums[i - 1]
    s = nums[i]
    if f == s:
        nums[i] = f + s
        nums.remove(nums[i - 1])
        i = 0
    i += 1

if len(nums) <= 1:
    print(nums[0])
else:
    print(" ".join(map(str, nums)))
