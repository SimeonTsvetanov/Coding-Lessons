board = []
for x in range(3):
    row = list(map(lambda x: int(x), input().split(" ")))
    board.append(row)

first_won = False
second_won = False

# rows and cols check
for row_col in range(3):
    if board[row_col][0] == board[row_col][1] and board[row_col][1] == board[row_col][2]:
        winner = board[row_col][0]
        if winner == 1:
            first_won = True
        elif winner == 2:
            second_won = True
    if board[0][row_col] == board[1][row_col] and board[1][row_col] == board[2][row_col]:
        winner = board[0][row_col]
        if winner == 1:
            first_won = True
        elif winner == 2:
            second_won = True

# first diagonal check
if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    winner = board[0][0]
    if winner == 1:
        first_won = True
    elif winner == 2:
        second_won = True

# second diagonal check
if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    winner = board[0][2]
    if winner == 1:
        first_won = True
    elif winner == 2:
        second_won = True

# print winner
if first_won:
    print("First player won")
elif second_won:
    print("Second player won")
else:
    print("Draw!")