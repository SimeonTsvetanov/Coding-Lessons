"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#4

SUPyF2 D.Types and Vars Exercise - 05. Print Part of the ASCII Table
Problem:
Find online more information about ASCII (American Standard Code for Information Interchange) and write a program
that prints part of the ASCII table of characters on the console.
On the first line of input you will receive the char index you should start with and on the second line -
the index of the last character you should print.

Examples
Input:	Output:
60
65	    < = > ? @ A

69
79	    E F G H I J K L M N O

97
104 	a b c d e f g h

40
55	    ( ) * + , - . / 0 1 2 3 4 5 6 7
"""
for symbol in range(int(input()), int(input()) + 1):
    print(chr(symbol), end=" ")
