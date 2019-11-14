"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/426#6

07. Largest N Elements

Problem:
Read a list of integers on the first line of the console. On the next line, you will receive an integer N.
After that, find and print the largest N items the list, sorted in descending order.
Examples
Input	                Output
5 3 4 1 2
3	                    5 4 3

11 872 673 1 2
2	                    872 673

11 52 43 12 1 6
4	                    52 43 12 11
Hints
- A possible solution to this problem is:
- Sort the list in descending order, using a sorting algorithm such as Insertion Sort,
- Extract the first N items from it
"""

nums = [int(item) for item in input().split(" ")]
count = int(input())

nums.sort(reverse=True)

start = 0
sorted_nums = []

while count != 0:
    sorted_nums += [nums[start]]
    start += 1
    count -= 1

for num in sorted_nums:
    print(num, end=" ")
