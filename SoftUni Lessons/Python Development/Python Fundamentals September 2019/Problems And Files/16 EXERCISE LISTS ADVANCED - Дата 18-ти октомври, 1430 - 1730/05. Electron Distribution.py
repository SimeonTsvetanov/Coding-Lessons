"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Compete/Index/1731#4

SUPyF2 Lists-Advanced-Exercise - 05. Electron Distribution

Problem:
You are a mad scientist and you decided to play with electron distribution among atom's shells.
You know that basic idea of electron distribution is that electrons should fill a shell until it's holding the maximum
number of electrons.
The rules for electron distribution are as follows:
•	Maximum number of electrons in a shell is distributed with a rule of 2n^2
        (n being position of a shell a.k.a the list index + 1).
•	For example, maximum number of electrons in 3rd shield is 2*3^2 = 18.
•	Electrons should fill the lowest level shell first.
•	If the electrons have completely filled the lowest level shell,
        the other unoccupied electrons will fill the higher level shell and so on.

Examples:
Input:	Output:
10  	[2, 8]
44  	[2, 8, 18, 16]
"""
total = int(input())

array = []
n = 1

while total > 0:
    el = 2 * (n ** 2)
    if el <= total:
        array.append(el)
        total -= el
    else:
        array.append(total)
        total -= el
    n += 1

print(array)
