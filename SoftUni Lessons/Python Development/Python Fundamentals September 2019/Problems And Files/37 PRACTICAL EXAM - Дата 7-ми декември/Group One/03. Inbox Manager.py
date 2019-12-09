"""
Programming Fundamentals Final Exam - 07 December 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/1928/Programming-Fundamentals-Final-Exam-07-December-2019-Group-1
name: Inbox manager
"""
users = {}

while True:
    command = input().split("->")
    if command[0] == "Statistics":
        break

    elif command[0] == "Add":
        add_username = command[1]
        if add_username not in users:
            users[add_username] = []
        else:
            print(f"{add_username} is already registered")

    elif command[0] == "Send":
        send_username = command[1]
        send_email = command[2]
        if send_username in users:
            users[send_username] += [send_email]

    elif command[0] == "Delete":
        delete_username = command[1]
        if delete_username in users:
            del users[delete_username]
        else:
            print(f"{delete_username} not found!")

print(f"Users count: {len(users)}")

for user, emails in sorted(users.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{user}")
    for email in emails:
        print(f" - {email}")
