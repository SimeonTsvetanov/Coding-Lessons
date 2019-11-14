"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1719#4
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise - 05. Can't Sleep? Count Sheep

Problem:
If you can't sleep, just count sheep! Given a non-negative integer, 3 for example, return a string with a murmur:
"1 sheep...2 sheep...3 sheep..." Input will always be valid, i.e. no negative integers.
"""
how_many_sheep = int(input())

for sheep in range(how_many_sheep):
    print(f"{sheep + 1} sheep...", end="")
