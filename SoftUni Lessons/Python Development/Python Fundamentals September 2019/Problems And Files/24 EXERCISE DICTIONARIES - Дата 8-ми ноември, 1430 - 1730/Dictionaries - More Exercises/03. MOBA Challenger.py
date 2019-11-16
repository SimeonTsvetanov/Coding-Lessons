"""
Dictionaries - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1738#2

SUPyF2 Dict-More-Ex. - 03. MOBA Challenger

Problem:
Pesho is a pro MOBA player, he is struggling to become а master of the Challenger tier.
So he watches carefully the statistics in the tier.
You will receive several input lines in one of the following formats:
"{player} -> {position} -> {skill}"
"{player} vs {player}"
The player and position are strings, the given skill will be an integer number. You need to keep track of every player.
When you receive a player and his position and skill, add him to the player pool, if he isn`t present,
else add his position and skill or update his skill, only if the current position skill is lower than the new value.
If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
Compare their positions, if they got at least one in common,
the player with better total skill points wins and the other is demoted from the tier -> remove him.
If they have same total skill points, the duel is tie and they both continue in the Season.
If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
You should end your program when you receive the command "Season end". At that point you should print the players,
ordered by total skill in desecending order,
then ordered by player name in ascending order.
Foreach player print their position and skill, ordered desecending by skill,
then ordered by position name in ascending order.
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	Player and position will always be one word string, containing no whitespaces.
•	Skill will be an integer in the range [0, 1000].
•	There will be no invalid input lines.
•	The programm ends when you receive the command "Season end".
Output
•	The output format for each player is:
"{player}: {totalSkill} skill"
"- {position} <::> {skill}"
Examples:
Input:
Pesho -> Adc -> 400
Gosho -> Jungle -> 300
Stamat -> Mid -> 200
Stamat -> Support -> 250
Season end

Output:
Stamat: 450 skill
- Support <::> 250
- Mid <::> 200
Pesho: 400 skill
- Adc <::> 400
Gosho: 300 skill
- Jungle <::> 300

Comments:
We order the players by total skill points descending, then by name.
We print every position along its skill ordered descending by skill, then by position name.

Input:
Pesho -> Adc -> 400
Bush -> Tank -> 150
Faker -> Mid -> 200
Faker -> Support -> 250
Faker -> Tank -> 250
Pesho vs Faker
Faker vs Bush
Faker vs Hide
Season end

Output:
Faker: 700 skill
- Support <::> 250
- Tank <::> 250
- Mid <::> 200
Pesho: 400 skill
- Adc <::> 400

Comments:
Faker and Pesho don`t have common position, so the duel isn`t valid.
Faker wins vs Bush /common position: "Tank". Bush is demoted.
Hide doesn`t exist so the duel isn`t valid.
We print every player left in the tier.
"""

# This was the Solution with Dictionaries
# TODO Judge 80/100 (last two tests are with invalid input)
"""
players_pool = {}

while True:
    command = input()
    if command == "Season end":
        break

    # Filling in players
    if "->" in command:
        player = command.split(" -> ")[0]
        position = command.split(" -> ")[1]
        skill = int(command.split(" -> ")[2])

        if player not in players_pool:
            players_pool[player] = {position: skill}
        elif player in players_pool:
            if position not in players_pool[player]:
                players_pool[player][position] = skill
            elif position in players_pool[player]:
                if skill > players_pool[player][position]:
                    players_pool[player][position] = skill

    # Time for battle:
    elif "vs" in command:
        player_one = command.split(" vs ")[0]
        player_two = command.split(" vs ")[1]

        if player_one in players_pool and player_two in players_pool:
            for position_player_one, skill_player_one in players_pool[player_one].items():
                for position_player_two, skill_player_two in players_pool[player_two].items():
                    if position_player_one == position_player_two:
                        if skill_player_one == skill_player_two:
                            continue
                        elif skill_player_one > skill_player_two:
                            players_pool.pop(player_two)
                        elif skill_player_two > skill_player_one:
                            players_pool.pop(player_one)

# print the players ordered and the total skill
for player, all_skills in sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(all_skills.values())} skill")
    for skill_name, skill_points in sorted(all_skills.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {skill_name} <::> {skill_points}")
"""

# Now as I'am to lazy to track Judge bugs. I have pirated a copy of Colleague in the university (Takvor G.)
# So I guess, ... if you ever see that : Thank you :D

moba = {}

while True:
    cin = input()

    if cin == "Season end":
        break

    if " -> " in cin:
        player, position, skill = cin.split(" -> ")
        skill = int(skill)

        if player not in moba:
            moba[player] = {}

        if position not in moba[player]:
            moba[player][position] = 0

        if moba[player][position] < skill:
            moba[player][position] = skill

    elif " vs " in cin:
        to_go = False
        player_a, player_b = cin.split(" vs ")
        if player_a in moba and player_b in moba:
            for pos in moba[player_a]:
                skill_a = moba[player_a][pos]
                if pos in moba[player_b]:
                    skill_b = moba[player_b][pos]
                    to_go = True
                    break  # Ox, Judge!
        if to_go:
            if skill_a > skill_b:  # Ox, Judge! Remove the player from contest!
                del moba[player_b]
                # if not len(moba[player_b]):
                #     del moba[player_b]
            elif skill_a < skill_b:
                del moba[player_a]
                # if not len(moba[player_a]):
                #     del moba[player_a]

players = {}
for player in moba:
    for pos in moba[player].items():
        if player not in players:
            players[player] = 0

        players[player] += pos[1]

sorted_players = sorted(sorted(players.items(), key=lambda kvp: kvp[0]), key=lambda kvp: kvp[1], reverse=True)

for item in sorted_players:
    print(f"{item[0]}: {item[1]} skill")
    sorted_positions = sorted(sorted(moba[item[0]].items(), key=lambda kvp: kvp[0]), key=lambda kvp: kvp[1],
                              reverse=True)
    for kvp in sorted_positions:
        print(f"- {kvp[0]} <::> {kvp[1]}")
