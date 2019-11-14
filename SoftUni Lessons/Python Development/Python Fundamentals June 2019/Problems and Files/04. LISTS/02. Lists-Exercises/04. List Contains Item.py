"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/426#0

01. Array Contains Element

Problem:
Read a list of integers on the first line of the console and an integer N from the second line of the console and print
whether the item is contained in the list. If it is, print “yes”, otherwise print “no”.
Examples:
Input:
1 2 3 4 5
5
Output: yes

Input:
8 7 7 9 6 2 2
11
Output: no
"""
nums = [int(item) for item in input().split(" ")]
num = int(input())

if num in nums:
    print("yes")
else:
    print("no")
