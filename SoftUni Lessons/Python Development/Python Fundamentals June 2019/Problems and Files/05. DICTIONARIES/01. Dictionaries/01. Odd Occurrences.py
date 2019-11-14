"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#0

SUPyF Dictionaries - 01. Odd Occurrences

Problem:
Write a program that extracts from a given sequence of words all elements that present in it odd number of times
(case-insensitive).
- Words are given in a single line, space separated.
- Print the result elements in lowercase, in their order of appearance.

Examples:
Input	                                    Output
Java C# PHP PHP JAVA C java             	java, c#, c
3 5 5 hi pi HO Hi 5 ho 3 hi pi	            5, hi
a a A SQL xx a xx a A a XX c	            a, SQL, xx, c
"""
words = [word for word in input().lower().split(" ")]

print_words = []
odd_occurrences = {}

for word in words:
    odd_occurrences[word] = words.count(word)

for item, value in odd_occurrences.items():
    if value % 2 != 0:
        print_words += [item]

print(", ".join(print_words))



