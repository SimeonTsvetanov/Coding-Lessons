"""
Lists Basics - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1726#3

SUPyF2 Lists More Exercise - 04. Battle Ships

Problem:
You will be given a number n representing the number of rows of the field.
On the next n lines you will receive each row of the field as a string with numbers separated by a space.
Each number greater than zero represents a ship with a health equal to the number value.
After that you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}".
Each time a square is being attacked, if there is a ship there (number greater than 0) you should reduce its value.
After the attacks have ended, print how many ships were destroyed (if its value has reached zero)

Example:
Input:
3
1 0 0 1
2 0 0 0
0 3 0 1
0-0 1-0 2-1 2-1 2-1 1-1 2-1

Output:
2
"""
rows = int(input())
all_ships = []
count_destroyed_ships = 0

for row in range(rows):
    all_ships += [[int(ship) for ship in input().split()]]
attacks = input().split(" ")

for attack in attacks:
    attack = attack.split("-")
    row = int(attack[0])
    col = int(attack[1])
    if all_ships[row][col] > 0:
        all_ships[row][col] -= 1
        if all_ships[row][col] == 0:
            count_destroyed_ships += 1


print(count_destroyed_ships)
