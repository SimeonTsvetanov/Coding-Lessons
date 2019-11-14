"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#4

SUPyF2 Lists-Advanced-Exercise - 06. Group of 10's

Problem:
Write a program that receives a list of numbers (string containing integers separated by ", ")
and prints lists with the numbers them into lists of 10's.
Examples:
•	The numbers 2 8 4 3 fall into the group under 10
•	The numbers 13 19 14 15 fall into the group under 20
For more details, see the examples below

Example:
Input	                            Output
8, 12, 38, 3, 17, 19, 25, 35, 50	Group of 10's: [8, 3]
                                    Group of 20's: [12, 17, 19]
                                    Group of 30's: [25]
                                    Group of 40's: [38, 35]
                                    Group of 50's: [50]

1, 3, 3, 4, 34, 35, 25, 21, 33	    Group of 10's: [1, 3, 3, 4]
                                    Group of 20's: []
                                    Group of 30's: [25, 21]
                                    Group of 40's: [34, 35, 33]
"""
a = [int(number) for number in input().split(", ")]

group = 10
group_list = []

while True:
    if len(a) == 0:
        break
    for i in a:
        if i <= group:
            group_list += [i]
    print(f"Group of {group}'s: [{', '.join(str(num) for num in group_list)}]")
    for digit in group_list:
        a.remove(digit)
    group += 10
    group_list = []
