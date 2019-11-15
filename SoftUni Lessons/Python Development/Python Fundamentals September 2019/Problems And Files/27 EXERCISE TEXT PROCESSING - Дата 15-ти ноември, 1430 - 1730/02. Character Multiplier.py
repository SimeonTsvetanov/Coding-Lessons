"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#1

SUPyF2 Text-Pr.-Ex. - 02. Character Multiplier

Problem:
Create a method that takes two strings as arguments and returns the sum of their character codes multiplied
(multiply str1[0] with str2[0] and add to the total sum). Then continue with the next two characters.
If one of the strings is longer than the other,
add the remaining character codes to the total sum without multiplication.

Examples
Input	        Output
Gosho Pesho	    53253
123 522	        7647
a aaaa	        9700
"""
"""
one, two = input().split()
total = 0
for i in range(max(len(one), len(two))):
    try:
        if one[i] and two[i]:
            total += (ord(one[i]) * ord(two[i]))
    except Exception:
        try:
            if one[i]:
                total += ord(one[i])
        except Exception:
            try:
                if two[i]:
                    total += ord(two[i])
            except Exception:
                continue
print(total)
"""

# Second Option from work at Class:

first_string, second_string = input().split()

total_sum = 0

for i in range(max(len(first_string), len(second_string))):
    if i < len(first_string) and i < len(second_string):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    else:
        if i < len(first_string):
            total_sum += ord(first_string[i])
        else:
            total_sum += ord(second_string[i])

print(total_sum)





























