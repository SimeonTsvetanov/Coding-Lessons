"""
Lists Basics - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1726#1

SUPyF2 Lists More Exercise - 02. Tic-Tac-Toe

Problem:
You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
Legend:
•	0 - empty space
•	1 - first player move
•	2 - second player move
Find out who the winner is. If the first player wins print "First player won", otherwise if the second player wins print
"Second player won", otherwise print "Draw!"
Example:
Input:
2 0 1
0 1 0
1 0 2
Output:
First player won

Input:
0 1 0
2 2 2
1 0 0

Output:
Second player won

Input:
1 0 2
0 1 2
1 2 0

Output:
Draw!
"""
r_1 = [int(digit) for digit in input().split()]
r_2 = [int(digit) for digit in input().split()]
r_3 = [int(digit) for digit in input().split()]

if r_1.count(r_1[0]) == len(r_1) and r_1[0] != 0:
    if sum(r_1) == 6:
        print(f"Second player won")
    else:
        print("First player won")
elif r_2.count(r_2[0]) == len(r_2) and r_2[0] != 0:
    if sum(r_2) == 6:
        print(f"Second player won")
    else:
        print("First player won")
elif r_3.count(r_3[0]) == len(r_3) and r_3[0] != 0:
    if sum(r_3) == 6:
        print(f"Second player won")
    else:
        print("First player won")
elif (r_1[0] == r_2[0] == r_3[0]) and r_1[0] != 0:
    if (r_1[0] + r_2[0] + r_3[0]) == 6:
        print(f"Second player won")
    else:
        print("First player won")
elif (r_1[1] == r_2[1] == r_3[1]) and r_1[1] != 0:
    if (r_1[1] + r_2[1] + r_3[1]) == 6:
        print(f"Second player won")
    else:
        print("First player won")
elif (r_1[2] == r_2[2] == r_3[2]) and r_1[2] != 0:
    if (r_1[2] + r_2[2] + r_3[2]) == 6:
        print(f"Second player won")
    else:
        print("First player won")
elif (r_1[0] == r_2[1] and r_1[0] == r_3[2]) and r_1[0] != 0:
    if r_1[0] == 2:
        print(f"Second player won")
    else:
        print("First player won")
elif (r_1[2] == r_2[1] and r_1[2] == r_3[0]) and r_1[0] != 0:
    if r_1[2] == 2:
        print(f"Second player won")
    else:
        print("First player won")
else:
    print("Draw!")
