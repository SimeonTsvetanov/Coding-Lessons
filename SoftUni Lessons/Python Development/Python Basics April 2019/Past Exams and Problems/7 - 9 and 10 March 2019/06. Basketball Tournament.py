tournament_name = None
count_games = 0
points_1 = 0
points_2 = 0
games_won = 0
games_lost = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break
    count_games = int(input())
    for game in range(1, count_games + 1):
        points_1 = int(input())
        points_2 = int(input())
        if points_1 > points_2:
            print(f"Game {game} of tournament {tournament_name}: win with {points_1 - points_2} points.")
            games_won += 1
        else:
            print(f"Game {game} of tournament {tournament_name}: lost with {points_2 - points_1} points.")
            games_lost += 1

total_games = games_won + games_lost

print(f"{(games_won / total_games * 100):.2f}% matches win")
print(f"{(games_lost / total_games * 100):.2f}% matches lost")
