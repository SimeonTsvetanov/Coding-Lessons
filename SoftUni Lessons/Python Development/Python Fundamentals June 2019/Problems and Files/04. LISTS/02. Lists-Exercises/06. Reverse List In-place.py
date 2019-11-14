"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/426#2

03. Reverse Array In-place

Problem:
Read a list of integers on the first line of the console. After that, reverse the list in-place
(as in, don’t create a new collection to hold the result, reverse it using only the original list).
After you are done, print the reversed list on the console.
Note: You are not allowed to iterate over the list backwards and just print it,
Examples
Input	            Output
1 2 3 4 5	        5 4 3 2 1
1 4 2 7 6 1 1	    1 1 6 7 2 4 1
11 52 43 12 1 6	    6 1 12 43 52 11
"""

nums = [int(item) for item in input().split(" ")]

nums.reverse()

for num in nums:
    print(num, end=" ")

