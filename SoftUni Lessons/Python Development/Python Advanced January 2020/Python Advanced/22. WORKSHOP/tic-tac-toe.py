from time import sleep

player_one = {"name": "", "symbol": "X"}
player_two = {"name": "AI", "symbol": "O"}
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
current_player = player_one

positions = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2]
}


def read_player_info():
    player_one["name"] = input("Player one name: ")
    # CODE WITHOUT AI
    # player_two["name"] = input("Player two name: ")
    # symbol = input(f"{player_one['name']} would you like to play with 'O' or 'X'? ")
    # while symbol != "X" and symbol != "O":
    #     symbol = input(f"{player_one['name']} would you like to play with 'O' or 'X'? ")
    # player_one["symbol"] = symbol
    # player_two["symbol"] = 'O' if player_one["symbol"] == 'X' else 'X'


def print_rules():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def play():
    current_move_symbol = input(f"{current_player['name']} choose a free spot from [1-9]: ")
    while current_move_symbol not in positions or board[positions[current_move_symbol][0]][positions[current_move_symbol][1]] != " ":
        current_move_symbol = input(f"{current_player['name']} choose a free spot from [1-9]: ")
    current_move = positions[current_move_symbol]
    board[current_move[0]][current_move[1]] = current_player["symbol"]


def check_game_won(player_symbol):
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


def check_game_tie():
    return not any(" " in row for row in board)


def switch_players():
    return player_one if current_player == player_two else player_two


def draw_board():
    for row in board:
        print("| " + " | ".join(row) + " |")


def minimax(is_maximizing):
    if check_game_won("X"):
        return -1
    if check_game_won("O"):
        return 1
    if check_game_tie():
        return 0

    if is_maximizing:
        best_score = -99999
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(False)
                    board[row][col] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = 99999
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(True)
                    board[row][col] = " "
                    best_score = min(best_score, score)
        return best_score


def ai_turn():
    best_score = -99999
    best_move = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                current_score = minimax(False)
                board[row][col] = " "
                if current_score > best_score:
                    best_score = current_score
                    best_move = [row, col]

    board[best_move[0]][best_move[1]] = "O"


# user input and rules
read_player_info()
print_rules()

# start playing the game
while True:
    # player move
    # REMOVE AI LOGIC FOR 2 PLAYERS
    if current_player == player_one:
        play()
    else:
        print("AI makes a move...")
        sleep(3)
        ai_turn()
    # draw board
    draw_board()
    # check game end
    if check_game_won(current_player['symbol']):
        print(f"{current_player['name']} won!")
        break
    if check_game_tie():
        print("Tie!")
        break
    # switch players
    current_player = switch_players()