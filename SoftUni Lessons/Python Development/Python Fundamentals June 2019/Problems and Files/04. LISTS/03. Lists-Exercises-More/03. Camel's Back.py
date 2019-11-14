"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/425#2

03. Camel's Back

Problem:
The city is breaking down on a camel back. You will receive a sequence of N integers, (space-separated),
which will represent the buildings in the city.  You will then receive an integer M, indicating the camel back's size.
The camel back is a linear structure standing below the city, in such a way that it has an equal amount of buildings
to its left and right. The idea is, if every round – one building falls from the left side of the city, and one from
the right side, how many rounds will it take for the city to stop breaking down?
As output you must print how many rounds it took before the city stopped breaking down as “{rounds} rounds”.
On the next line, print what’s left of the city (space-separated). Format: “remaining: {buildings (space-separated)}”
If no buildings have fallen, print “already stable: {buildings (space-separated)}”
Example: city with 9 elements; Camel back size: 5
"""

nums = [int(item) for item in input().split(" ")]
m = int(input())

count_rounds = 0

while len(nums) != m:
    nums.pop(0)
    nums.pop(len(nums) - 1)
    count_rounds += 1

if count_rounds == 0:
    print(f"already stable: ", end="")
    for num in nums:
        print(num, end=" ")
    print()
else:
    print(f"{count_rounds} rounds")
    print(f"remaining: ", end="")
    for num in nums:
        print(num, end=" ")
    print()
