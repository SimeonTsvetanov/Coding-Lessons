"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#0

SUPyF2 Lists-Advanced-Exercise - 01. Which Are In?

Problem:
Given two lists of strings print a new list of the strings that contains words from the first list
which are substrings of any of the strings in the second list (only unique values)

Input
There will be 2 lines of input: the two lists separated by ", "

Output
Print the resulting list on the console

Example
Input:
arp, live, strong
lively, alive, harp, sharp, armstrong
Output:
['arp', 'live', 'strong']

Input:
tarp mice bull
lively alive harp sharp armstrong

Output:
[]
"""
words_1 = input().split(", ")
words_2 = input().split(", ")
words_3 = []
for word_1 in words_1:
    for word_2 in words_2:
        if word_1 in word_2:
            if word_1 not in words_3:
                words_3.append(word_1)
print(words_3)

