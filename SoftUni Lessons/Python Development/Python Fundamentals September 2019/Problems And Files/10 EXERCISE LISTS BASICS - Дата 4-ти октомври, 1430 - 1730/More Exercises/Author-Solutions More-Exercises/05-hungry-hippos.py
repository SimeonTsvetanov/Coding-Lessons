rows = int(input())
board = []

def mark_neighbors(row, col):
    # use recursion to mark all the neighbor ones, and their neighbor ones and so on, until no neighbors are left. So we make sure that if a 1 is marked, no other ones that are attached to it will not be marked as a separate leap
    board[row][col] = -1
    if row + 1 < len(board) and board[row + 1][col] == 1:
        mark_neighbors(row + 1, col)
    if row - 1 >= 0 and board[row - 1][col] == 1:
        mark_neighbors(row - 1, col)
    if col + 1 < len(board[row]) and board[row][col + 1] == 1:
        mark_neighbors(row, col + 1)
    if col - 1 >= 0 and board[row][col - 1] == 1:
        mark_neighbors(row, col - 1)

for x in range(rows):
    row = list(map(lambda x: int(x), input().split(" ")))
    board.append(row)

leaps = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        # if a 1 is found mark it as a leap
        if board[i][j] == 1:
            leaps += 1
            mark_neighbors(i, j)

print(leaps)