def get_input():
    return [[int(r) for r in input().split(' ')] for _ in range(3)]


def check_game_won(board, player_symbol):
    for row in board:
        if row.count(player_symbol) == 3:
            return True
    for col in range(3):
        if all(board[i][col] == player_symbol for i in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player_symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player_symbol:
        return True
    return False


def print_result(input_field):
    if check_game_won(input_field, 1):
        print(f"First player won")
    elif check_game_won(input_field, 2):
        print(f"Second player won")
    else:
        print(f"Draw!")


def run():
    print_result(get_input())


if __name__ == '__main__':
    run()
