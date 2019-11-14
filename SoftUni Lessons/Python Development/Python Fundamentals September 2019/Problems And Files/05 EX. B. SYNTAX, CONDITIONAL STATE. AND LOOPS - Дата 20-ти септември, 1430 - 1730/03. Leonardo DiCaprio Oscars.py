"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#2
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 03. Leonardo DiCaprio Oscars

Problem:
Write a program that receives a single integer number and prints different messages depending on the number:
-	If Oscar is 88 - "Leo finally won the Oscar! Leo is happy".
-	If Oscar is 86 - "Not even for Wolf of Wall Street?!"
-	If Oscar is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
-	If Oscar is over 88 - "Leo got one already!"

Examples:
Input:	Output:
88	    Leo finally won the Oscar! Leo is happy
86	    Not even for Wolf of Wall Street?!
81	    When will you give Leo an Oscar?
89	    Leo got one already!
"""
oscar = int(input())

if oscar == 88:
    print("Leo finally won the Oscar! Leo is happy")
elif oscar == 86:
    print("Not even for Wolf of Wall Street?!")
elif oscar < 88:
    print("When will you give Leo an Oscar?")
else:
    print("Leo got one already!")
