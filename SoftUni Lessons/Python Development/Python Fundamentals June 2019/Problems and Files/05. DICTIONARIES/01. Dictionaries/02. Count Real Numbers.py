"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#1

SUPyF Dictionaries - 02. Count Real Numbers

Problem:
Read a list of real numbers and print them in ascending order along with their number of occurrences.

Examples:
Input:                  Output:
8 2.5 2.5 8 2.5         2.5 -> 3 times
                        8 -> 2 times
---------------------------------------
Input:                  Output:
1.5 5 1.5 3             1.5 -> 2 times
                        3 -> 1 times
                        5 -> 1 times
----------------------------------------
Input:                  Output:
-2 0.33 0.33 2          -2 -> 1 times
                        0.33 -> 2 times
                        2 -> 1 times

Hints:
- Use dictionary (key=nums, value=count) named counts.
- Pass through each input number num and increase counts[num] (when num exists in the dictionary)
 or assign counts[num] = 1 (when num does not exist in the dictionary).
- Pass through all numbers num in the dictionary (counts.keys())
 and print the number num and its count of occurrences counts[num].
"""
nums = [float(item) for item in input().split(" ")]

nums.sort()

counts = {}

for num in nums:
    if num not in counts:
        counts[num] = nums.count(num)

for key, value in counts.items():
    print(f"{key} -> {value} times")
