"""
Exam Preparation Programming Fundamentals Final Exam Retake - 9 August 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1767#0

Name: Username

Problem:
Pesho has decided to finally make an account on social media. His problem is that too many people are called Pesho too,
so he needs a program that will help him generate an original username and he is asking you for help.
First, you are going to receive the username that he wants to use in the first place, then commands.
You will be receiving commands until the "Sign up" command. There are six possible commands:
•	"Case {lower/upper}"
o	Replace all letters with lower case or with upper case, then print the result.
•	"Reverse {startIndex} {endIndex}"
o	Reverse the substring from the startIndex until the endIndex, then print it. Do NOT change it in the username.
Note: Check if the indexes are valid. If they aren’t - skip the command. The indexes are inclusive.
•	"Cut {substring}"
o	Check if the string contains  the substring and if yes, cut it out and print the result.
o	If the string doesn’t contain the given substring, print:
"The word {string} doesn't contain {substring}."
•	"Replace {char}"
o	Replace all occurences of char with astericks (*) and print the result.
•	"Check {char}"
o	In order for a username to be valid, it must contain the given char.
o	If the password is valid, print "Valid". If it is not valid, print: "Your username must contain {char}."
Input
•	On the 1st line you are going to receive the string.
•	On the next lines, until the "Sign up" command is received, you will be receiving commands.
•	All commands are case sensitive.
Output
•	Print the output of every command in the format described above.

Examples:
Input:
Pesho
Case lower
Cut ES
Check @
Sign up

Output:
pesho
The word pesho doesn't contain ES.
Your username must contain @.

Input:
ThisIsMyString
Reverse 1 4
Replace i
Cut My
Sign up

Output:
Isih
Th*sIsMyStr*ng
Th*sIsStr*ng
"""

# This is my initial solution using only Functions:
username = input()


def case(lower_or_upper: str):
    global username
    username = eval(f"username.{lower_or_upper}()")
    print(username)


def reverse(start_index: int, end_index: int, current_username: str):
    if 0 <= start_index < end_index < len(current_username):
        reversed_part = username[start_index:end_index+1][::-1]
        print(reversed_part)


def cut(substring: str):
    global username
    if substring in username:
        username = username.replace(substring, "")
        print(username)
    elif substring not in username:
        print(f"The word {username} doesn't contain {substring}.")


def replace(char: str):
    global username
    username = username.replace(char, "*")
    print(username)


def check(char: str, current_username: str):
    if char in current_username:
        print("Valid")
    elif char not in current_username:
        print(f"Your username must contain {char}.")


def main():
    while True:
        command = input().split()

        if command[0] == "Sign":
            break

        elif command[0] == "Case":
            case(lower_or_upper=command[1])

        elif command[0] == "Reverse":
            reverse(start_index=int(command[1]), end_index=int(command[2]), current_username=username)

        elif command[0] == "Cut":
            cut(substring=command[1])

        elif command[0] == "Replace":
            replace(char=command[1])

        elif command[0] == "Check":
            check(char=command[1], current_username=username)


if __name__ == '__main__':
    main()
