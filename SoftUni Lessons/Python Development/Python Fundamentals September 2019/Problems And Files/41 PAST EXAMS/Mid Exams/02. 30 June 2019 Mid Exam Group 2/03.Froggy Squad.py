"""
Programming Fundamentals Mid Exam - 30 June 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1683#2

SUPyF2 P.-Mid-Exam/30 June 2019/2. - Froggy Squad

Problem:
Create a program that helps you keep track of the frogs that are on the riverside.
Because you are an extreme animal lover, you also name them.
You will receive the names of the frogs that are already on the riverside on a single line,
separated by a single space in the following format:
"{frog1} {frog2} {frog3}… {frogn}"
Then you will receive commands that describe their action. There are five possible commands:
•	"Join {name}":
o	A frog comes on the riverside and you need to add it in the end of your collection. Frog names will never repeat.
•	"Jump {name} {index}"
o	A frog jumps out of the water and joins the other frogs.
You need to add it in your collection on the given index, if the index exists.
•	"Dive {index}":
o	The frog on the given index has decided to jump into the water.
You have to remove it from your collection, if the index exists.
•	"First/Last {count}":
o	Print the first/last {count} frogs separated by a single space.
If the count requested is more than the frogs- just print them to the end.
"{frog} {frog} {frog}"
•	"Print Normal/Reversed"
o	Print the names of the frogs in your collection in normal
    (in the order they have been added) or reversed order in the format described below, then stop the program:
"Frogs: {frog1} {frog2}… {frogn}"
Input
•	On the 1st line, you will receive the starting list with the names of the frogs separated by a single space.
•	On the next lines, you will receive commands in the format described above.
Output
•	Print the list after the manipulations upon the "Print" command in the format described above.

Examples:
Input:
Blake Muggy Kishko
Join Kvachko
Dive 0
First 10
Print Reversed

Output:
Muggy Kishko Kvachko
Frogs: Kvachko Kishko Muggy

Comments:
First, we receive the "Join Kvachko" command, so we add the frog in the end of the collection.
Then, we receive the command "Dive  0", so we remove the frog on index 0.
Also, we receive the command "First 10", which is more than the frogs we have, so we print all frogs instead.
Lastly, we have to print the collection in reversed, so our output is: "Frogs: Kvachko Kishko Muggy".

Input:
A B C D E F
Join G
Jump Q 3
Last 3
Dive 2
Print Normal

Output:
E F G
Frogs: A B Q D E F G
"""
frogs = input().split()

while True:
    command = input().split()
    if command[0] == "Join":
        frogs.append(command[1])
    elif command[0] == "Jump":
        name, index = command[1], int(command[2])
        if 0 <= index < len(frogs):
            frogs.insert(index, name)
    elif command[0] == "Dive":
        index = int(command[1])
        if 0 <= index < len(frogs):
            frogs.pop(index)
    elif command[0] == "First" or command[0] == "Last":
        count = min(int(command[1]), len(frogs))
        if command[0] == "First":
            print(' '.join(frogs[:count]))
        elif command[0] == "Last":
            print(' '.join(frogs[-count:]))
    elif command[0] == "Print":
        if command[1] == "Normal":
            print(f"Frogs: {' '.join(frogs)}")
        elif command[1] == "Reversed":
            print(f"Frogs: {' '.join(frogs[::-1])}")
        break
