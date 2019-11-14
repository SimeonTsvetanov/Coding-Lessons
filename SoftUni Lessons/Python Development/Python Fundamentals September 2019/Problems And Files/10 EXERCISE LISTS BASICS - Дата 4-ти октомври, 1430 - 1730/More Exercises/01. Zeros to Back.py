"""
Lists Basics - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1726#0

SUPyF2 Lists More Exercise - 01. Zeros to Back

Problem:
Write a program that receives a single string (integers separated by a comma and space ", "),
finds all the zeros and moves them to the back without messing up the other elements. Print the resulting integer list
Example:
Input:
1, 0, 1, 2, 0, 1, 3
Output:
[1, 1, 2, 1, 3, 0, 0]
"""
numbers = [int(number) for number in input().split(", ")]
for number in numbers:
    if number == 0:
        numbers.append(number)
        numbers.remove(number)
print(numbers)
