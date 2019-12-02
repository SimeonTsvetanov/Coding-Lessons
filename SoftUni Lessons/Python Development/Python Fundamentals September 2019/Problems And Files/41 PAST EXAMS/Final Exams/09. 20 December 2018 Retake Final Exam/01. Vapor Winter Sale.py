"""
Technology Fundamentals Retake Final Exam - 20 December 2018
link: https://judge.softuni.bg/Contests/Practice/Index/1394#0
Name: 01. Vapor Winter Sale
"""
all_games = {}

games = input().split(", ")
for game in games:
    if "-" in game:
        name = game.split("-")[0]
        price = float(game.split("-")[1])
        if name not in all_games:
            all_games[name] = [price]

    elif ":" in game:
        name = game.split(":")[0]
        dlc = game.split(":")[1]
        if name in all_games:
            all_games[name][0] += all_games[name][0] * 0.2
            all_games[name] += [dlc]

for game, items in all_games.items():
    if len(items) == 1:
        all_games[game][0] -= all_games[game][0] * 0.2
    elif len(items) == 2:
        all_games[game][0] -= all_games[game][0] * 0.5

for game, items in sorted(all_games.items(), key=lambda x: x[1][0]):
    if len(items) == 2:
        print(f"{game} - {items[1]} - {items[0]:.2f}")

for game, items in sorted(all_games.items(), key=lambda x: -x[1][0]):
    if len(items) == 1:
        print(f"{game} - {items[0]:.2f}")
