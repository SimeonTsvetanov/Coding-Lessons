"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1511#2

SUPyF Exam 10.03.2019 - 03. Listmons DB

Problem:
Input / Constraints
Listmon is as like a Google. It tracks every of its players in the game. You beat It in its own game,
so It asks you now to help It with the database and make several reports for It, because it is a mess there.
You will start receiving players data in format:
{playerName} -> {resultOfTheGame}, {resultOfTheGame}, {resultOfTheGame}, {resultOfTheGame} ...
Keep in mind that it is possible to have two players with the same playerName. You should store the data separately,
not replacing it.
Every line is different data and different player.
You must store it until you receive command 'report'. After that you will receive reporting tickets in format:
•	score descending
•	score ascending
•	numberOfGames descending
•	numberOfGames ascending
Output
* If you receive 'score descending' you must print all players by the order of the score descending,
after that by name ascending in format:
     {name}: {score}
* If you receive 'score ascending' you must print all players by the order of the score ascending,
after that by name ascending in format:
     {name}: {score}
* If you receive 'number of games descending' you must print all players by the number of games played descending,
after that by name ascending in format:
     {name}: {count of the games}
* If you receive 'number of games ascending’  you must print all players by the number of games played ascending
after that by name ascending in format:
     {name}: {count of the games}

Examples:

Input:
Sims -> 15, 25, 65, 85
Misho -> 5, 5, 5
Azzi -> 0, 0, 2, 5
Sims -> 5, 5, 5, 5, 5, 5, 5
report
score ascending
end

Output:
Azzi: 7
Misho: 15
Sims: 35
Sims: 190

Input:
theBest -> 952, 26, 83, 15, 25
ultimatePlayer -> 1998, 0, 25
nick_name -> 25, 0, 9852648
report
numberOfGames descending
numberOfGames ascending
end

Output:
theBest: 5
nick_name: 3
ultimatePlayer: 3
nick_name: 3
ultimatePlayer: 3
theBest: 5
"""


class Player:
    def __init__(self, name: str, score: int, games: int):
        self.name = name
        self.score = score
        self.games = games


all_players = []

while True:
    data = input()
    if data == "report":
        break
    name_player, all_scores = data.split(" -> ")
    scores_in_list = [int(item) for item in all_scores.split(", ")]
    total_score = sum(scores_in_list)
    games_played = len(scores_in_list)
    player = Player(name=name_player, score=total_score, games=games_played)
    all_players += [player]

while True:
    command = input()
    if command == "end":
        break

    elif command == "score descending":
        score_d_list = sorted(sorted(all_players, key=lambda x: x.name), key=lambda x: x.score, reverse=True)
        for player in score_d_list:
            print(f"{player.name}: {player.score}")

    elif command == "score ascending":
        score_a_list = sorted(sorted(all_players, key=lambda x: x.name), key=lambda x: x.score)
        for player in score_a_list:
            print(f"{player.name}: {player.score}")

    elif command == "numberOfGames descending":
        games_d_list = sorted(sorted(all_players, key=lambda x: x.name), key=lambda x: x.games, reverse=True)
        for player in games_d_list:
            print(f"{player.name}: {player.games}")

    elif command == "numberOfGames ascending":
        games_a_list = sorted(sorted(all_players, key=lambda x: x.name), key=lambda x: x.games)
        for player in games_a_list:
            print(f"{player.name}: {player.games}")
