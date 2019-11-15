"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#5

SUPyF2 Text-Pr.-Ex. - 06. Replace Repeating Chars

Problem:
Write a program that reads a string from the console and replaces any sequence of the same letters
 with a single corresponding letter.
Examples
Input	                    Output
aaaaabbbbbcdddeeeedssaa	    abcdedsa
qqqwerqwecccwd	            qwerqwecwd
"""

# This was the initial Solution
"""
past_letter = ""
for i in input():
    if len(past_letter) == 0:
        past_letter = i
    else:
        if i == past_letter[-1]:
            pass
        else:
            past_letter += i
print(past_letter)
"""

# This is the solution in class:
text = input()
i = 0

while i < len(text) - 1:
    if text[i] == text[i + 1]:
        text = text.replace(f"{text[i]}{text[i + 1]}", f"{text[i]}")
        i -= 1
    i += 1
print(text)











