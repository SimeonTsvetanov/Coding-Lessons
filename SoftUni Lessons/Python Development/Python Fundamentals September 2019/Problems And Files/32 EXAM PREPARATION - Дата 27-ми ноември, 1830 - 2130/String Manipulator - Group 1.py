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
