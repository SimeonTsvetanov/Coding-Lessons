"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/425#0

01. Distinct List

Problem:
You will be given a list of integers on the first line of the input (space-separated).
Remove all repeating elements from the list.

Examples:
Input	                Output	                Comments
1 2 3 4	                1 2 3 4	                No repeating elements
7 8 9 7 2 3 4 1 2	    7 8 9 2 3 4 1	        7 and 2 are already present in the list >>> remove them
20 8 12 13 4 4 8 5	    20 8 12 13 4 5	        4 and 8 are already present in the list >>> remove them
"""

nums = [int(item) for item in input().split(" ")]

for num in nums:
    while nums.count(num) != 1:
        nums.reverse()
        nums.remove(num)
        nums.reverse()

for num in nums:
    print(num, end=" ")
