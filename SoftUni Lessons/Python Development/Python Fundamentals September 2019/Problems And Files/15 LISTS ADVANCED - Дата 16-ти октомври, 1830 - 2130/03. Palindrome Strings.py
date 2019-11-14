"""
Lists Advanced - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1730#2

SUPyF2 Lists-Advanced-Lab - 03. Palindrome Strings

Problem:
Write a program that receives on the first line words separated by a space and a searched palindrome on the second.
Print all the palindromes on the first line. Print all the occurrences of the searched palindrome in the format:
"Found palindrome {count} times"

Examples:
Input:	                                Output:
wow father mom wow shirt stats          ['wow', 'mom', 'wow', 'stats']
wow	                                    Found palindrome 2 times

hey how you doin? lol                   ['lol']
mom                                     Found palindrome 0 times
"""
strings = [word for word in input().split()]
print([word for word in strings if word == word[::-1]])
special_word = input()
print(f"Found palindrome {len([word for word in strings if word == special_word])} times")
