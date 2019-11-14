n = int(input())

board = []

for x in range(n):
    row = list(map(lambda x: int(x), input().split(" ")))
    board.append(row)

attacks = list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), input().split(" ")))
defeated_count = 0

for attack in attacks:
    row = attack[0]
    col = attack[1]
    if board[row][col] > 0:
        board[row][col] -= 1
        if board[row][col] == 0:
            defeated_count += 1

print(defeated_count)