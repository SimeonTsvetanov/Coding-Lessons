users = {}
submissions = {}

while True:
    command = input().split('-')

    if command[0] == 'exam finished':
        break

    if len(command) == 3:
        username = command[0]
        language = command[1]
        points = int(command[2])

        if username not in users:
            users[username] = {language: points}
            if language not in submissions:
                submissions[language] = 0
            submissions[language] += 1
        else:
            if language not in users[username]:
                users[username] = {language: points}
                if language not in submissions:
                    submissions[language] = 0
                submissions[language] += 1
            else:
                users[username][language] = max(users[username][language], points)
                if language not in submissions:
                    submissions[language] = 0
                submissions[language] += 1
    else:
        username = command[0]
        if username in users:
            del users[username]


print(f"Results:")
for user, languages in users.items():
    for language, points in languages.items():
        print(f"{user} | {points}")
print(f"Submissions:")
for submission, count in submissions.items():
    print(f"{submission} - {count}")
