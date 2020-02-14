galaxy = [[x for x in input()] for _ in range(int(input()))]  # Create the Galaxy

steven_position = []  # Lets get Stephan Start position and the Black Holes if any:
black_holes = [[], []]  # I'am storing the black holes in matrix :D
for row in range(len(galaxy)):
    for col in range(len(galaxy[row])):
        if galaxy[row][col] == "S":
            steven_position = [row, col]
        if galaxy[row][col] == "O":
            if not black_holes[0]:
                black_holes[0] = [row, col]
            else:
                black_holes[1] = [row, col]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

star_power = 0
out_of_space = False
while star_power < 50 and not out_of_space:
    move = directions[input()]
    if (0 <= (steven_position[0] + move[0]) < len(galaxy)) and (0 <= (steven_position[1] + move[1]) < len(galaxy)):
        # Then the move is possible

        # First Check for the Black Hole:
        if galaxy[steven_position[0] + move[0]][steven_position[1] + move[1]] == "O":  # He goes in the black hole:
            for hole in range(len(black_holes)):
                if (black_holes[hole][0] == (steven_position[0] + move[0])) \
                        and (black_holes[hole][1] == (steven_position[1] + move[1])):
                    black_holes.pop(hole)
                    galaxy[steven_position[0]][steven_position[1]] = "-"
                    galaxy[steven_position[0] + move[0]][steven_position[1] + move[1]] = "-"
                    galaxy[black_holes[0][0]][black_holes[0][1]] = "S"
                    steven_position = [black_holes[0][0], black_holes[0][1]]
                    break

        # And then check for the numbers:
        elif galaxy[steven_position[0] + move[0]][steven_position[1] + move[1]] != "-":
            star_power += int(galaxy[steven_position[0] + move[0]][steven_position[1] + move[1]])
            galaxy[steven_position[0]][steven_position[1]] = "-"
            galaxy[steven_position[0] + move[0]][steven_position[1] + move[1]] = "S"
            steven_position = [steven_position[0] + move[0], steven_position[1] + move[1]]

        # And if its not a soldier or Helen so it's just a empty cell:
        else:
            galaxy[steven_position[0]][steven_position[1]] = "-"
            galaxy[steven_position[0] + move[0]][steven_position[1] + move[1]] = "S"
            steven_position = [steven_position[0] + move[0], steven_position[1] + move[1]]

    else:
        # The move is impossible and he flies out of the galaxy
        out_of_space = True
        galaxy[steven_position[0]][steven_position[1]] = "-"
        break

if out_of_space:
    print(f"Bad news, the spaceship went to the void.")
else:
    # star_power >= 50:
    print(f"Good news! Stephen succeeded in collecting enough star power!")
print(f"Star power collected: {star_power}")
[print(''.join(row)) for row in galaxy]  # Print the galaxy
