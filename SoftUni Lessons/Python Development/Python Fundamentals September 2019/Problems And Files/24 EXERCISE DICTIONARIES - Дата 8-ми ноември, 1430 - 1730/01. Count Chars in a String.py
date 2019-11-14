"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#0

SUPyF2 Dict-Exercise - 01. Count Chars in a String

Problem:
Write a program that counts all characters in a string except for space (' ').
Print all the occurrences in the following format:
{char} -> {occurrences}
Examples
Input:	            Output:
text	            t -> 2
                    e -> 1
                    x -> 1

text text text      t -> 6
                    e -> 3
                    x -> 3
"""
characters = {}

list_of_characters = [symbol for symbol in input() if symbol != " "]
for symbol in list_of_characters:
    if symbol not in characters:
        characters[symbol] = 1
    else:
        characters[symbol] += 1

for character, occurrence in characters.items():
    print(f"{character} -> {occurrence}")


