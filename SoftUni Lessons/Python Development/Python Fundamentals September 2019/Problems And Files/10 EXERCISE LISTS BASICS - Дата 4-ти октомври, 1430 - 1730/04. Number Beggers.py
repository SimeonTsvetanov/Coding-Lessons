"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#3

SUPyF2 Lists Basics Exercise - 04. Number Beggers

Problem:
Your task here is pretty simple: given a list of numbers and an amount of beggars,
you are supposed to return a list with the sum of what each beggar brings home, assuming they all take regular turns,
from the first to the last.
For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5],
the second collects [2,4].
The same list with 3 beggars would have in turn have produced a better outcome for the second beggar: 5, 7 and 3,
as they will respectively take [1, 4], [2, 5] and [3].
Also note that not all beggars have to take the same amount of "offers",
meaning that the length of the list is not necessarily a multiple of n; length can be even shorter,
in which case the last beggars will of course take nothing (0).
Input
You will receive 2 lines of input: a single string containing the numbers separated by a comma and a space ", ".
On the second line you will receive the number of beggars
Output
Print a list of all the sums that each beggar made
Example:
/-------------------------/-----------------------/
/ Input	                  /  Output               /
/-------------------------/-----------------------/
/ 1, 2, 3, 4, 5           /                       /
/ 2	                      /  [9, 6]               /
/-------------------------/-----------------------/
/ 3, 4, 5, 1, 29, 4       /                       /
/ 6	                      /  [3, 4, 5, 1, 29, 4]  /
/-------------------------/-----------------------/
/ 100, 94, 24, 99         /                       /
/ 5	                      /  [100, 94, 24, 99, 0] /
/-------------------------/-----------------------/
"""
numbers = [int(number) for number in input().split(", ")]
beggars_list = [0] * int(input())
counter = 0

for number in numbers:
    beggars_list[counter] += number
    counter += 1
    if counter == len(beggars_list):
        counter = 0
print(beggars_list)
