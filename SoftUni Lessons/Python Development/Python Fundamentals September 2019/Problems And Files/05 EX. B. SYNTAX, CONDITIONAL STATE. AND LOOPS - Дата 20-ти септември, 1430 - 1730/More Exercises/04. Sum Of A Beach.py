"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1720#3
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise More - 04. Sum Of A Beach

Problem:
Beaches are filled with sand, water, fish, and sun. Given a string,
calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (regardless of the case).
Examples:
Input:                          Output:
WAtErSlIde	                    1
GolDeNSanDyWateRyBeaChSuNN	    3
gOfIshsunesunFiSh	            4
cItYTowNcARShoW	                0
"""
text = input().lower()

counter = 0

counter += text.count("sand")
counter += text.count("water")
counter += text.count("fish")
counter += text.count("sun")

print(counter)


