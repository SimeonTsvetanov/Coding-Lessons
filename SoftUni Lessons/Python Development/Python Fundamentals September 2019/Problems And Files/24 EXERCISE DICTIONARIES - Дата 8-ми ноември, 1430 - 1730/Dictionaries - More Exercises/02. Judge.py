"""
Dictionaries - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1738#1

SUPyF2 Dict-More-Ex. - 02. Judge

Problem:
You know the jude system, right?! Your job is to create a program similar to the Judge system.
You will receive several input lines in one of the following formats:
{username} -> {contest} -> {points}
The constestName and username are strings, the given points will be an integer number.
You need to keep track of every contest and individual statistics of every user.
You should check if such contest already exists, and if not, add it,
otherwise check if the current user Is participating in the contest, if he is participating take the higher score,
otherwise just add it.
Also you need to keep individual statistics for each user - the total points of all constests.
You should end your program when you receive the command "no more time".
At that point you should print each contest in order of input,
for each contest print the participants ordered by points in desecending order, than ordered by name in ascending order.
After that, you should print individual statistics for every participant ordered by total points in desecnding order,
and then by alphabetical order.
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	Username and contest name always will be one word.
•	Points will be an integer will be an integer in range [0, 1000].
•	There will be no invalid input lines.
•	If all sorting criteria fail, the order should be by order of input.
•	The input ends when you receive the command "no more time".
Output
•	The output format for the contests is:
{constestName}: {participants.Count} participants
{position}. {username} <::> {points}
•	After you print all contests, print the individual statistics for every participant.
•	The output format is:
Individual standings:
{position}. {username} -> {totalPoints}
Examples:
Input:
Pesho -> Algo -> 400
Gosho -> Algo -> 300
Stamat -> Algo -> 200
Pesho -> DS -> 150
Mimi -> DS -> 600
no more time

Output:
Algo: 3 participants
1. Pesho <::> 400
2. Gosho <::> 300
3. Stamat <::> 200
DS: 2 participants
1. Mimi <::> 600
2. Pesho <::> 150
Individual standings:
1. Mimi -> 600
2. Pesho -> 550
3. Gosho -> 300
4. Stamat -> 200

Input:
Pesho -> OOP -> 350
Gosho -> OOP -> 250
Stamat -> Advanced -> 600
Gosho -> OOP -> 300
Prakash -> OOP -> 300
Prakash -> Advanced -> 250
Ani -> JSCore -> 400
no more time

Output:
OOP: 3 participants
1. Pesho <::> 350
2. Gosho <::> 300
3. Prakash <::> 300
Advanced: 2 participants
1. Stamat <::> 600
2. Prakash <::> 250
JSCore: 1 participants
1. Ani <::> 400
Individual standings:
1. Stamat -> 600
2. Prakash -> 550
3. Ani -> 400
4. Pesho -> 350
5. Gosho -> 300
"""
contests = {}
individual_standings = {}

while True:
    # Getting the input sorted
    command = input().split(" -> ")
    if command[0] == "no more time":
        break
    username = command[0]
    contest = command[1]
    points = int(command[2])

    # Filling the contests dictionary
    if contest not in contests:
        contests[contest] = {username: points}
    elif contest in contests:
        if username not in contests[contest]:
            contests[contest][username] = points
        elif username in contests[contest]:
            if points > contests[contest][username]:
                contests[contest][username] = points

# Filling the individual standings dictionary:
for contest, value in contests.items():
    for username, points in value.items():
        if username not in individual_standings:
            individual_standings[username] = points
        elif username in individual_standings:
            individual_standings[username] += points

# Printing the contests, sorted as required.
for contest, value in contests.items():
    print(f"{contest}: {len(value)} participants")
    number = 1
    for name, score in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{number}. {name} <::> {score}")
        number += 1

# Printing the individual standings, sorted as required.
print("Individual standings:")
position = 1
for user, score in sorted(individual_standings.items(), key=lambda x: (-x[1], x[0])):
    print(f"{position}. {user} -> {score}")
    position += 1
