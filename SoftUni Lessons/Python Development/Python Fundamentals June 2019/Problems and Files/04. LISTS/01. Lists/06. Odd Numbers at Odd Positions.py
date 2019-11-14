"""
Lists
Проверка: https://judge.softuni.bg/Contests/Practice/Index/924#5

06. Odd Numbers at Odd Positions

Условие:
Write a program to read a list of integers and find how many odd numbers at odd positions the list holds.
If there are no numbers, which match this criteria, do not print anything
Examples:

Input:
2 3 5 2 7 9 -1 -7
Output:
Index 1 -> 3
Index 5 -> 9
Index 7 -> -7

Input:
2 3 55 2 4 1
Output:
Index 1 -> 3
Index 5 -> 1

Input:
5 0 1 2
Output:
(no output)

Hints
-Positions are counted from 0 from left to right, so if for example the second item (index 1) is odd,
then we should count it, and so on…
-Do NOT count odd numbers, which are at even positions (0, 2, 4, etc…)
"""

"""
How I solved it:

First we will take all the added integers on one line divided by space and it will add them in a new list one by one:
Then we will create a counter so it will know which is the index position of the current check.
Then using For Loop for each item in the list we will check first if the Counter is odd and if so we will check if the
current checked item is odd and if so: We will print the output. 
Even if the counter is odd or even outside of the IF check we need to add 1 to it.  
"""
nums = [int(item) for item in input().split(" ")]
counter = 0
for item in nums:
    if counter % 2 != 0:
        if item % 2 != 0:
            print(f"Index {counter} -> {item}")
    counter += 1


