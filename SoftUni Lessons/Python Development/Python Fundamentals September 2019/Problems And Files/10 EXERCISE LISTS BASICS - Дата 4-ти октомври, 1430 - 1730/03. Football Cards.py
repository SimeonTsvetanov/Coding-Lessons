"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#2

SUPyF2 Lists Basics Exercise - 03. Football Cards

Problem:
Most football fans love it for the goals and excitement. Well, this problem doesn't.
You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining,
the game is stopped immediately by the referee, and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g the card 'B-7'
means player #7 from team B received a card. (index 6 of the list)
The task: Given a list of cards (could be empty),
return the number of remaining players on each team at the end of the game in the format:
"Team A - {players_count}; Team B - {players_count}".
If the game was terminated print an additional line: "Game was terminated"
Note for the random tests: If a player that has already been sent off receives another card - ignore it.
Input
The input (the cards) will come on a single line separated by a single space
Output
Print the remaining players as described above and add another line (as shown above) if the game was terminated

Example
Input:                          Output:
A-1 A-5 A-10 B-2	            Team A - 7; Team B - 9
-------------------------------------------------------
A-1 A-5 A-10 B-2 A-10 A-7	    Team A - 6; Team B - 9
                                Game was terminated
"""
team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
game_terminated = False

red_cards = [player for player in input().split(" ")]
for player in red_cards:
    if "A" in player and player in team_A:
        team_A.remove(player)
    if "B" in player and player in team_B:
        team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_terminated:
    print("Game was terminated")


