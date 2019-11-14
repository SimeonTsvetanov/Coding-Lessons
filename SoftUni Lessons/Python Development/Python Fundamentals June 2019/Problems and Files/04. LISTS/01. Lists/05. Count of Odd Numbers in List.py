"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#4

05. Count of Odd Numbers in List

Условие:
Write a program to read a list of integers and find how many odd items it holds.
Examples
Input	            Output
1 -2 3 4	        2
3 9 -9 -6 1 -2	    4
66 0 2 1	        1
Hints:
-You can check if a number is odd if you divide them by 2 and check whether you get a remainder of 1.
-Odd numbers, which are negative, have a remainder of -1.
"""

"""
How I solved it:

First we will take all the added integers on one line divided by space and it will add them in a new list one by one:
Then, we need to create a count_of_odd_numbers variable so we can store the count there.
Next, we will create a For Loop to check for each number in the list, if its Odd. And if its odd we will add 1 to the
odd_nums counter
And finally to print the output:
"""

# print(len([num for num in [int(item) for item in input().split(" ")] if num % 2 != 0]))

nums = [int(item) for item in input().split(" ")]

odd_nums_count = 0

for item in nums:
    if item % 2 != 0:
        odd_nums_count += 1

print(odd_nums_count)
