"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#5

SUPyF2 Lists Basics Exercise - 06. Survival of the Biggest

Problem:
Write a program that receives a list of integer numbers and a number n.
The number n represents the amount of numbers to remove from the list. You should remove the smallest ones
Input
On the first line you will receive a string (numbers separated by a space),
on the second line you will receive a number n (count of numbers to remove)
Output
Print all the numbers that are left in the list
Example:
Input:
10 9 8 7 6 5
3
Output:
[10, 9, 8]
Input:
1 10 2 9 3 8
2
Output:
[10, 9, 3, 8]
"""
numbers = [int(number) for number in input().split()]
times_to_remove = int(input())
for each_time in range(times_to_remove):
    numbers.remove(min(numbers))
print(numbers)

