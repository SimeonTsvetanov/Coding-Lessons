"""
Text Processing - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1739#3

SUPyF2 Text-Processing-Lab - 04. Text Filter

Problem:
Write a program that takes a text and a string of banned words.
All words included in the ban list should be replaced with asterisks "*", equal to the word's length.
The entries in the ban list will be separated by a comma and space ", ".
The ban list should be entered on the first input line and the text on the second input line.

Examples:
Input:
Linux, Windows
It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client

Output:
It is not *****, it is GNU/*****. ***** is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/*****! Sincerely, a ******* client
"""
banned_words = input().split(", ")
text = input()
for word in banned_words:
    text = text.replace(word, f"{'*' * len(word)}")
print(text)
