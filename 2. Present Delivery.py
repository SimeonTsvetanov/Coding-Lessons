count_of_presents = int(input())
size_of_neighborhood = int(input())

happy_kids_count = 0

# This are the delta changes (not sure if I know how to use them yet, but still :D)
moves = {
    'up': [-1, 0],
    'down': [+1, 0],
    'left': [0, -1],
    'right': [0, +1]
}

# Create the matrix - neighborhood
neighborhood = []
for line in range(size_of_neighborhood):
    neighborhood.append([x for x in input().split()])

# Get Santa First Position:
santa_position = []
for row in range(len(neighborhood)):
    for col in range(len(neighborhood[0])):
        if neighborhood[row][col] == "S":
            santa_position = [row, col]
            break

while True:
    # First we check if we have to end the program
    if count_of_presents <= 0:
        break
    command = input()
    if command == "Christmas morning":
        break

    move = ""
    if command == "up":
        move = "up"
    elif command == "down":
        move = "down"
    elif command == "left":
        move = "left"
    elif command == "right":
        move = "right"
    next_row = santa_position[0] + moves[move][0]
    next_col = santa_position[1] + moves[move][1]

    if neighborhood[next_row][next_col] == "X" or neighborhood[next_row][next_col] == "-":
        neighborhood[santa_position[0]][santa_position[1]] = "-"
        santa_position = [next_row, next_col]
        neighborhood[next_row][next_col] = "S"

    elif neighborhood[next_row][next_col] == "V":
        count_of_presents -= 1
        happy_kids_count += 1
        neighborhood[santa_position[0]][santa_position[1]] = "-"
        santa_position = [next_row, next_col]
        neighborhood[next_row][next_col] = "S"

    elif neighborhood[next_row][next_col] == "C":
        neighborhood[santa_position[0]][santa_position[1]] = "-"
        santa_position = [next_row, next_col]
        neighborhood[next_row][next_col] = "S"
        for move_direction, position in moves.items():
            if count_of_presents <= 0:
                break
            if neighborhood[santa_position[0] + position[0]][santa_position[1] + position[1]] == "V" or \
                    neighborhood[santa_position[0] + position[0]][santa_position[1] + position[1]] == "X":
                neighborhood[santa_position[0] + position[0]][santa_position[1] + position[1]] = "-"
                count_of_presents -= 1
                happy_kids_count += 1

nice_kids_left_without_presents = sum([street.count("V") for street in neighborhood])

if count_of_presents == 0 and nice_kids_left_without_presents - happy_kids_count != 0:
    print(f"Santa ran out of presents!")

for street in neighborhood:
    print(*street)
if nice_kids_left_without_presents > 0:
    print(f"No presents for {nice_kids_left_without_presents} nice kid/s.")
else:
    print(f"Good job, Santa! {happy_kids_count} happy nice kid/s.")
