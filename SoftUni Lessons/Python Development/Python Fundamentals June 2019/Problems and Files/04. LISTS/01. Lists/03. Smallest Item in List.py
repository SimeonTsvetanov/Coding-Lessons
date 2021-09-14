"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#2

03. Smallest Item in List

Условие:
Write a program to read a list of integers, find the smallest item and print it.
Examples

Input	            Output
1 2 3 4	            1
3 2 9 -9 6 1	    -9
-6 0 -17 -1	        -17

Hints
Loop through the integer list until you find the smallest item
"""

# We can handle this in a few ways: First - will be as it's asked for in the problem:

"""
import sys
nums = [int(item) for item in input().split(" ")]

min_number = sys.maxsize

for item in nums:
    if item < min_number:
        min_number = item

print(min_number)
"""

# but much easier way will be to use the build function in Python for checking the minimum value in list:
"""
nums = [int(item) for item in input().split(" ")]
print(min(nums))
"""
# And finally we could join them all together in one line:

print(min([int(item) for item in input().split(" ")]))

# """
# Write a program to read a list of integers, find the smallest item and print it.
# Examples
# 
# Input	                Output
# 1 2 3 4	                1
# 3 2 9 -9 6 1	        -9
# -6 0 -17 -1	            -17
# 
# Hints
# •	Loop through the integer list until you find the smallest item
# """
# 
# print(min([int(num) for num in input().split(" ")]))
# 

