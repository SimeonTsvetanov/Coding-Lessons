"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1578#1

SUPyF Exam Preparation 2 - 02 Lists
Problem:
Input / Constraints
You will be given a single lines of elements(integers), separated with one or more spaces.
You should check if all elements in the line are unique.
If they are you should increase the value of every even element with the number of 2 and print the list on single row
in ascending order separated by ",".
If they are not unique you should increase every odd element with the number of 3 and print them on single row,
separated with ":"
On the next line you should print sum of the all elements divided by the count of the elements in the list.
You should do that until you receive the command "stop playing"
Output
If the elements are unique
Unique list: {elements in the list, separated by “,”}
Output: {sum of all elements divided by the length of the list}
Else
Non-unique list: {elements in the list, separated by “:”}
Output: {sum of all elements divided by the length of the list}

Examples:
---------
Input:
1 2  3   4 5 6
1 1 2   2 1 4 7 7 8 8
 5 5 5 5
stop playing

Output:
Unique list: 1,3,4,5,6,8
Output: 4.50
Non-unique list: 2:2:4:4:4:4:8:8:10:10
Output: 5.60
Non-unique list: 8:8:8:8
Output: 8.00

Input:
1      1 1
stop playing

Output:
Non-unique list: 4:4:4
Output: 4.00
"""

while True:
    command = input()
    if command == "stop playing":
        break
    nums = [int(item) for item in command.split()]
    if_unique = len(set(nums)) == len(nums)
    if if_unique:
        nums = sorted([item + 2 if item % 2 == 0 else item for item in nums])
        print(f"Unique list: {','.join([str(item) for item in nums])}")
        print(f"Output: {(sum(nums) / len(nums)):.2f}")
    else:
        nums = sorted([item + 3 if item % 2 != 0 else item for item in nums])
        print(f"Non-unique list: {':'.join([str(item) for item in nums])}")
        print(f"Output: {(sum(nums) / len(nums)):.2f}")
