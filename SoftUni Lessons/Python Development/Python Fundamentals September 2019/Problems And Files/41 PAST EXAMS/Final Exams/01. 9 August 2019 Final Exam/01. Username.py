"""
Programming Fundamentals Final Exam Retake - 9 August 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1767#0

SUPyF2 P.-F.-Exam/9 August 2019. - 01. Username

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
pesho
The word pesho doesn't contain ES.
Your username must contain @.

Output:
Isih
Th*sIsMyStr*ng
Th*sIsStr*ng
"""

name = input()
while True:
    command = input().split()
    if command[0] == "Sign":
        break
    # Case Converting to lower or upper:
    if command[0] == "Case":
        if command[1] == "lower":
            name = name.lower()
        elif command[1] == "upper":
            name = name.upper()
        print(name)
    # Reverse from start to end index:
    elif command[0] == "Reverse":
        start, end = int(command[1]), int(command[2])
        if 0 <= start <= len(name) and start < end <= (len(name)):
            print(name[start:end + 1][::-1])
    # Cut a portion of the name if it exists:
    elif command[0] == "Cut":
        if command[1] in name:
            name = name.replace(command[1], "")
            print(name)
        else:
            print(f"The word {name} doesn't contain {command[1]}.")
    # Replace the char with *:
    elif command[0] == "Replace":
        name = ''.join(["*" if letter == command[1] else letter for letter in name])
        print(name)
    # Check if symbol is in name:
    elif command[0] == "Check":
        if command[1] in name:
            print("Valid")
        else:
            print(f"Your username must contain {command[1]}.")
