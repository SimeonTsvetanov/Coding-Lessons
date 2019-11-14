"""
Text Processing - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1739#1

SUPyF2 Text-Processing-Lab - 02. Repeat Strings

Problem:
Write a program that reads an array of strings.
Each string is repeated N times, where N is the length of the string. Print the concatenated string.

Examples:
Input:          Output:
hi abc add      hihiabcabcabcaddaddadd
work            workworkworkwork
ball            ballballballball
"""

# Solution #1:
# strings = input().split()
# result = ""
# for word in strings:
#     length = len(word)
#     result += word * length
# print(result)

# Solution #2:
print(''.join([word * len(word) for word in input().split()]))

