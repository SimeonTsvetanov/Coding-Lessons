players = {}

while True:
    command = input()
    if command == "Season end":
        break
    if ' -> ' in command:
        player, position, skill = command.split(' -> ')
        if player not in players:
            players[player] = {}
        if position not in players[player]:
            players[player][position] = 0
        players[player][position] = max(players[player][position], int(skill))
    elif ' vs ' in command:
        playerOne, playerTwo = command.split(' vs ')
        if (playerOne not in players) or (playerTwo not in players):
            continue
        fight_over = False
        for position_one, skill_one in players[playerOne].items():
            if fight_over:
                break
            for position_two, skill_two in players[playerTwo].items():
                if fight_over:
                    break
                if position_one == position_two:
                    total_skill_one = sum(players[playerOne].values())
                    total_skill_two = sum(players[playerTwo].values())
                    if total_skill_one > total_skill_two:
                        del players[playerTwo]
                        fight_over = True
                    elif total_skill_two > total_skill_one:
                        del players[playerOne]
                        fight_over = True
                    else:
                        fight_over = True


for player, positions in sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(positions.values())} skill")
    for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
