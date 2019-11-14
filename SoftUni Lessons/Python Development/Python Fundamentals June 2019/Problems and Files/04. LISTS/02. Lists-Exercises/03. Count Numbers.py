"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/423#6

07. Count Numbers

Problem:
Read a list of integers in range [0…1000] and print them in ascending order along with their number of occurrences.
Examples
Input	            Output
8 2 2 8 2 2 3 7    	2 -> 4
                    3 -> 1
                    7 -> 1
                    8 -> 2

10 8 8 10 10	    8 -> 2
                    10 -> 3
Hints
Several algorithms can solve this problem:
- Use an list count to count in counts[x] the occurrences of each item x.
- Sort the numbers and count occurrences of each number.
"""

nums = [int(item) for item in input().split(" ")]
nums.sort()

i = None

for num in nums:
    if i == num:
        continue
    print(f'{num} -> {nums.count(num)}')
    i = num

