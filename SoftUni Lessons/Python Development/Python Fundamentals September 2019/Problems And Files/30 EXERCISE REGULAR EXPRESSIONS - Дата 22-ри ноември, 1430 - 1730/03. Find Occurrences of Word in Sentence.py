"""
Regular Expressions - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1743#2

Name: 03. Find Occurrences of Word in Sentence

Problem:
Write a program that finds, how many times a given word, is used in a given sentence.
Note that letter case does not matter – it is case-insensitive.
The output is a single number indicating the amount of times the sentence contains the word.

Examples:

Input:
The waterfall was so high, that the child couldn't see its peak.
the
Output:
2

Input:
How do you plan on achieving that? How? How can you even think of that?
how
Output:
3

Input:
There was one. Therefore I bought it. I wouldn't buy it otherwise.
there
Output:
1
"""
import re

text = input()
word = input()
# pattern = r"\b" + re.escape(word) + r"\b"
pattern = rf"\b{word}\b"
matches = re.findall(pattern, text, re.I)
print(len(matches))
