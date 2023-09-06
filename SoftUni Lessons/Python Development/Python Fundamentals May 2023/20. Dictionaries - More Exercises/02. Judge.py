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



