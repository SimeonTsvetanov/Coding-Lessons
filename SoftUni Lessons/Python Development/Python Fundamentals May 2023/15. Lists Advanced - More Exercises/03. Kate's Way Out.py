"""
Lists Advanced - More Exercises - sold before!
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1732#4

SUPyF2 Lists Advanced-More-Ex. - 05. Kate's Way Out

Problem:
Kate is stuck into a maze, you have to help her to find her way out
On the first line you will be given how many rows there are in the maze.
On the next n lines you will be given the maze itself. Here is a legend for the maze:
•	"#" - means a wall; Kate cannot go through there
•	" " - means empty space; Kate can go through there
•	"k" - the initial position of Kate; start looking for a way out from there
There are two options: Kate either gets out or not. If Kate can get out print the following:
"Kate got out in {number_of_moves} moves". Otherwise print: "Kate cannot get out"
Examples
Input	    Output
4           Kate got out in 5 moves
######
##  k#
## ###
## ###

5           Kate cannot get out
######
##  k#
## ###
######
## ###
"""
rows = int(input())

maze = []

for i in range(rows):
    maze += [[symbol for symbol in input()]]

moves = 1
kate_out = False
condition = False
while True:
    if condition or kate_out:
        break
    for row in maze:
        if condition or kate_out:
            break
        for position in row:
            if position == "k":
                current_row = maze.index(row)
                index_kate = row.index("k")
                down_index = maze.index(row) + 1
                left_index = row.index("k") - 1
                right_index = row.index("k") + 1

                if maze[down_index][index_kate] == " ":
                    maze[down_index - 1][index_kate] = " "
                    maze[down_index][index_kate] = "k"
                    moves += 1
                    if current_row + 1 == maze.index(maze[-1]):
                        kate_out = True
                    break

                elif maze[current_row][left_index] == " ":
                    maze[current_row][left_index] = "k"
                    maze[current_row][index_kate] = " "
                    moves += 1
                    break
                else:
                    condition = True

if kate_out:
    print(f"Kate got out in {moves} moves")
else:
    print("Kate cannot get out")
