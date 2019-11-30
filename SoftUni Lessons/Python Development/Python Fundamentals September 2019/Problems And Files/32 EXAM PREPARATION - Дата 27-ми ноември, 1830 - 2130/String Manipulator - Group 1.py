"""
Exam Preparation Programming Fundamentals Final Exam - 03 August 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1748#0

Name: String Manipulator - Group 1

Problem:
Create a program that executes changes over a string. First, you are going to receive the string, then commands.
You will be receiving commands until the "End" command. There are six possible commands:
"Translate {char} {replacement}"
Replace all occurences of {char} with {replacement}, then print the string.
"Includes {string}"
Check if the string includes {string} and print "True/False".
"Start {string}"
Check if the string starts with {string} and print "True/False".
"Lowercase"
Make the whole string lowercased, then print it.
"FindIndex {char}"
Find the last index of {char}, then print it.
"Remove {startIndex} {count}"
Remove {count} characters from the string, starting from {startIndex}, then print it.
Input
On the 1st line you are going to receive the string.
On the next lines, until the "End" command is received, you will be receiving commands.
All commands are case sensitive.
The input will always be valid.
Output
Print the output of every command in the format described above.

Examples:
Input:
//Thi5 I5 MY 5trING!//
Translate 5 s
Includes string
Start //This
Lowercase
FindIndex i
Remove 0 10
End
Output:
//This Is MY strING!//
False
True
//this is my string!//
16
my string!//
"""

# This is the solution from in class:
"""
string = input()

com = input()
while com != "End":
    com = com.split(" ")
    command = com[0]

    if command == "Translate":
        char = com[1]
        repl = com[2]
        string = string.replace(char, repl)
        print(string)

    elif command == "Includes":
        char = com[1]
        if char in string:
            print("True")
        else:
            print("False")

    elif command == "Start":
        start = com[1]
        print(string.startswith(start))

    elif command == "Lowercase":
        string = string.lower()
        print(string)

    elif command == "FindIndex":
        char = com[1]
        print(string.rfind(char))

    elif command == "Remove":
        start = int(com[1])
        count = int(com[2])
        string = string.replace(string[start:start+count], "")
        print(string)

    com = input()
"""

# And this was mine solution: 
import re

text = input()

while True:
    command = input().split()
    if command[0] == "End":
        break

    elif command[0] == "Translate":
        char_to_replace = command[1]
        replacement = command[2]
        text = re.sub(char_to_replace, replacement, text)  # Replace all the letters with the new ones
        print(text)

    elif command[0] == "Includes":
        string_to_include = command[1]
        if string_to_include in text:
            print("True")
        else:
            print("False")

    elif command[0] == "Start":
        word_to_start = command[1]
        if text.startswith(word_to_start):
            print("True")
        else:
            print("False")

    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)

    elif command[0] == "FindIndex":
        last_character = command[1]
        index = text.rindex(last_character)
        print(index)

    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        stop_index = start_index + count
        text = text[:start_index] + text[stop_index::]
        print(text)
