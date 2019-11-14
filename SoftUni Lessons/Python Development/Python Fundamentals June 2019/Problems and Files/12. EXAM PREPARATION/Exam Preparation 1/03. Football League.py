"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/967#2

SUPyF Exam Preparation 1 - 03. Football League

Problem:
You will be given information about results of football matches. Create a standings table by points.
For win the team gets 3 points, for loss – 0 and for draw – 1.
Also find the top 3 teams with most scored goals in descending order.
If two or more teams are with same goals scored or same points order them by name in ascending order.
The name of each team is encrypted. You must decrypt it before proceeding with calculating statistics.
You will be given some string key and the team name will be placed between that key in reversed order.
For example: the key: “???”;
String to decrypt: “kfle???airagluB???gertIt%%” -> “airagluB” -> “Bulgaria”
Also you should ignore the letter casing in the team names. For example:
buLgariA = BulGAria = bulGARIA = BULGARIA
Input / Constraints
•	On the first line of input you will get the key that will be used for decryption
•	On the next lines until you receive “final” you will get lines in format:
{encrypted teamA} {encrypted teamB} {teamA score}:{teamB score}
•	Team scores will be integer numbers in the range [0...231]
Output
•	Print the standings table ordered descending by points in format:
Where place is a number in range [1… number of teams].
•	Then you should print the top 3 team ordered by goals in descending order in format:
•	All team’s names should be uppercase.
•	For more clarification, see the examples on the next page.

Examples:
Input:
??
??ecnarF?? ??kramneD?? 0:0
..??airagluB??32 ??dnalgnE??gf 3:2
Fg??NIAPS?? fgdrt%#$??YNAMREG??gtr 3:4
??eCnArF?? >>??yLATi??<< 2:2
final

Output:
League standings:
1. BULGARIA 3
2. GERMANY 3
3. FRANCE 2
4. DENMARK 1
5. ITALY 1
6. ENGLAND 0
7. SPAIN 0
Top 3 scored goals:
- GERMANY -> 4
- BULGARIA -> 3
- SPAIN -> 3

Input:
KZL
fdKZLairagluBKZL KZLkramneDKZLll 2:0
kzljjjKZLAiRaGluBKZL KZLylATIKZLkk 1:1
KZLkRamnedKZL KZLYlatiKZL 4:4
final

Output:
League standings:
1. BULGARIA 4
2. ITALY 2
3. DENMARK 1
Top 3 scored goals:
- ITALY -> 5
- DENMARK -> 4
- BULGARIA -> 3
"""

teams = {}

key = input()
while True:
    command = input()
    if command == "final":
        break
    team_1_encrypted, team_2_encrypted, result = command.split()
    goals_team_1, goals_team_2 = (int(item) for item in result.split(":"))
    team1 = ((team_1_encrypted.split(key))[1].split(key)[0])[::-1].upper()
    team2 = ((team_2_encrypted.split(key))[1].split(key)[0])[::-1].upper()
    team1_score_points = 0
    team2_score_points = 0
    if goals_team_1 == goals_team_2:
        team1_score_points = 1
        team2_score_points = 1
    elif goals_team_1 > goals_team_2:
        team1_score_points = 3
    elif goals_team_2 > goals_team_1:
        team2_score_points = 3

    if team1 not in teams:
        teams[team1] = []
        teams[team1] += [team1_score_points, goals_team_1]
    else:
        a = teams[team1]
        a[0] += team1_score_points
        a[1] += goals_team_1
        teams[team1] = a
    if team2 not in teams.keys():
        teams[team2] = []
        teams[team2] += [team2_score_points, goals_team_2]
    else:
        a = teams[team2]
        a[0] += team2_score_points
        a[1] += goals_team_2
        teams[team2] = a

place = 1
print("League standings:")
for key, value in sorted(sorted(teams.items(), key=lambda kv: kv[0]), key=lambda key_: key_[1][0], reverse=True):
    print(f"{place}. {key} {value[0]}")
    place += 1

counter = 0

print("Top 3 scored goals:")
for key, value in sorted(sorted(teams.items(), key=lambda kv: kv[0]), key=lambda key_: key_[1][1], reverse=True):
    print(f"- {key} -> {value[1]}")
    counter += 1
    if counter == 3:
        break
