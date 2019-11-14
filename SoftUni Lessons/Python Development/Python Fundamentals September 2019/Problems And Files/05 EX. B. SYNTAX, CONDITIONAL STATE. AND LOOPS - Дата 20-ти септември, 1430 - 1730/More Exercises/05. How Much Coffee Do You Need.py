"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1720#4
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise More - 05. How Much Coffee Do You Need?

Problem:

Everybody know that you passed to much time awake during night time...
Your task here is to define how much coffee you need to stay awake after your night.
Until you receive the command "END", you need to read a single command,
according to this command you will print the number of coffee you need to stay awake during day time.

Note: If the count exceed 5 please return 'You need extra sleep'.

The list of events can contain the following:
•	You have homework to do ('coding').
•	You have a dog or a cat that just decide to wake up too early ('dog' or 'cat').
•	You just watch a movie ('movie').
•	Other events can be present and it will be represent by arbitrary string, just ignore this one.

Each event can be lowercase, or uppercase.
If it is lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.

Input:
dog
CAT
gaming
END
Output:
3

Input:
movie
CODING
MOVIE
CLEANING
cat
END
Output:
You need extra sleep
"""
coffees = 0
while True:
    command = input()
    if command == "END":
        break
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)

