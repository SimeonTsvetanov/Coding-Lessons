# You will be given a number n representing the number of rows of the field
n = int(input())

# On the following n lines, you will receive
# each field row as a string with numbers separated by a space. Each number greater than zero represents a ship
# with health equal to the number value.

field = [[int(n) for n in input().split(' ')] for _ in range(n)]
# [print(n) for n in field]

# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}"
squares = [[int(n) for n in x.split('-')] for x in input().split(' ')]

# Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1.
# If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.
destroyed_ships = 0

for square in squares:
    x, y = square
    if field[x][y] > 0:
        field[x][y] -= 1
        if field[x][y] == 0:
            destroyed_ships += 1

print(destroyed_ships)
