"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/425#1

02. Integer Insertion

Problem:
You will receive a list of integers on the same line (separated by one space).
On the next lines, you will start receiving a list of strings, until you receive the string “end”.
Your task is to insert each string (converted to integer) at a specific index in the list.
The index is determined by the first digit of the number.
Example: 514 >>> first digit – 5 >>> insert 514 at the 5th index of the list.
After you insert all the elements, print the list, separated by single spaces.
The input will always be valid and you don’t need to explicitly check if you’re inserting an element into a valid index.

Examples:
Input:                              Output:
1 2 3 4 5 6 7 8 9                   1 1982 2 2 2772 25 3 4 5 8534 6 716 7 8 9
25
716
2772
1982
8534
2
end

Input:                              Output:
3 12 66 243 8766                    3 12 12 33 66 56 243 8766
12
33
56
end

Input:                              Output:
9 9 9 9 9 9 9 9 9 9                 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
9
9
9
9
9
end
"""

nums = [int(item) for item in input().split(" ")]

while True:
    string = input()
    if string == "end":
        break
    integer = int(string)
    first_num = int(string[0])
    nums.insert(first_num, integer)

for num in nums:
    print(num, end=" ")
