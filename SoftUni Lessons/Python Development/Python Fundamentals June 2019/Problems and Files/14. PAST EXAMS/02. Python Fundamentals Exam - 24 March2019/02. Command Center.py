"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1590#1

SUPyF Exam 24.03.2019 - 02. Command Center

Problem:
Input / Constraints
We are going to receive a list of integers from console.
After that we will start receive some of the following commands in format:
•	swap {index1} {index2}
•	enumerate_list
•	max
•	min
•	get_divisible by {number}

*If you receive command 'swap' you should check if the indexes are valid. A valid index is index which is 0 or higher
and is less than list length.
    -   If one of the indexes is not valid just print the list without changing it
    -   If both indexes are valid swap the two elements on these indexes

*If you receive ‘enumerate_list’ you should enumerate the list and print it in the following format:
    [(0, {list[0]}), (1, list[1]), (2, list[2]), (3, list[3])]
Where {list[n]} is the element corresponding to the given index (starting from zero)

*If you receive 'max', print the max number in the list
*If you receive 'min', print the min number in the list

*If you receive ‘get_divisible by’ you must print every element in the list which residue after division with {number}
is 0 in format:
[el1, el2, ….]
It is guaranteed -  the {number} never will be 0, so you do not need to check it.

Output
When you receive a command which says 'end', you should print the count of commands you have performed.
Note that invalid commands may appear. In this case do not print anything and do not count these commands as performed.

Examples:
    Input:
        1 3 2 4 5
        swap 1 15
        enumerate_list
        max
        get_divisible by 13
        get_divisible by 2
        swap 1 4
        enumerate_listtt
        end
    Output:
        [1, 3, 2, 4, 5]
        [(0, 1), (1, 3), (2, 2), (3, 4), (4, 5)]
        5
        []
        [2, 4]
        [1, 5, 2, 4, 3]
        6
    Input:
        15 -1 3 0 19 -15 24
        swap 0 1
        swap 4 6
        enumerate_list
        swap 6 1
        swap 7 -1
        get divisible by -15
        get_divisible by 15
        get_divisibleee by 15
        end
    Output:
        [-1, 15, 3, 0, 19, -15, 24]
        [-1, 15, 3, 0, 24, -15, 19]
        [(0, -1), (1, 15), (2, 3), (3, 0), (4, 24), (5, -15), (6, 19)]
        [-1, 19, 3, 0, 24, -15, 15]
        [-1, 19, 3, 0, 24, -15, 15]
        [0, -15, 15]
        6
"""

nums = [int(item) for item in input().split(" ")]

valid_operations = 0

while True:
    command = input()
    if command == "end":
        break
    a = [item for item in command.split(" ")]
    if a[0] == "swap" and len(a) == 3:
        if 0 <= int(a[1]) <= len(nums) and 0 <= int(a[2]) < len(nums):
            nums[int(a[1])], nums[int(a[2])] = nums[int(a[2])], nums[int(a[1])]
            print(nums)
            valid_operations += 1
        else:
            print(nums)
            valid_operations += 1
    elif command == "enumerate_list":
        print(list(enumerate(nums, 0)))
        valid_operations += 1
    elif command == "max":
        print(max(nums))
        valid_operations += 1
    elif command == "min":
        print(min(nums))
        valid_operations += 1
    elif a[0] == "get_divisible" and a[1] == "by" and len(a) == 3:
        divisible_list = []
        for num in nums:
            if num % int(a[2]) == 0:
                divisible_list += [num]
        print(divisible_list)
        valid_operations += 1

print(valid_operations)
