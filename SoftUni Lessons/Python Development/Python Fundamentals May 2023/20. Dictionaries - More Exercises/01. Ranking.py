contests = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(':')
    contests[contest] = password

users = {}

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split('=>')
    if (contest in contests) and (contests[contest] == password):
        if username not in users:
            users[username] = {}
        if contest not in users[username]:
            users[username][contest] = 0
        users[username][contest] = max(users[username][contest], int(points))

best_candidate = ["", 0]
for user, scores in users.items():
    sum_score = sum(scores.values())
    if sum_score >= best_candidate[1]:
        best_candidate[0], best_candidate[1] = user, sum_score

print(f"Best candidate is {best_candidate[0]} with total {best_candidate[1]} points.")
print(f"Ranking: ")
for user, content in sorted(users.items(), key=lambda x: x):
    print(user)
    for contest, points in sorted(users[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")


