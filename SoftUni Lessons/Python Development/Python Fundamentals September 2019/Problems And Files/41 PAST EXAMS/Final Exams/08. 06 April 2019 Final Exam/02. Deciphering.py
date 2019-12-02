"""
(Demo) Technology Fundamentals Final Exam - 06 April 2019
link: https://judge.softuni.bg/Contests/Practice/Index/1628#1
Name: 02. Deciphering
"""
valid_letters = "defghijklmnopqrstuvwxyz{}|#"
encrypted_string = input()
two_substrings = input().split(" ")
real_string = ''.join([chr(ord(letter) - 3) for letter in encrypted_string])
not_valid = False
for letter in encrypted_string:
    if letter not in valid_letters:
        not_valid = True
        break

if not not_valid:
    real_string = real_string.replace(two_substrings[0], two_substrings[1])
    print(real_string)
else:
    print("This is not the book you are looking for.")
