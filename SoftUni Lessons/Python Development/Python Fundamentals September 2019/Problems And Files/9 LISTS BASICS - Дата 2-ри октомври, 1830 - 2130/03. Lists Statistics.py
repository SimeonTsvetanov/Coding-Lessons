"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#2

SUPyF2 Lists Basics Lab - 03. Lists Statistics

Problem:
You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
•	One with all the positives (including 0)
•	One with all the negatives
Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"

Example:
Input:
5
10
3
2
-15
-4

Output:
[10, 3, 2]
[-15, -4]
Count of positives: 3. Sum of negatives: -19
"""
positive_list = []
negative_list = []

for how_many_times in range(int(input())):
    digit = int(input())
    if digit >= 0:
        positive_list += [digit]
    else:
        negative_list += [digit]

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")
