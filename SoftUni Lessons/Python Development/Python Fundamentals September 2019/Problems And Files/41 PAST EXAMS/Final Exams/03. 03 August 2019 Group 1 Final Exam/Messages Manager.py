"""
Exam Preparation Programming Fundamentals Final Exam - 03 August 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1748#2

Name: Messages Manager

Problem:
Create a program that manages messages sent and received of users. You need to keep information about username,
their sent and received messages. You will receive the capacity of possible messages kept at once per user.
You will be receiving lines with commands until you receive the "Statistics" command.
There are three possible commands:
"Add={username}={sent}={received}":
Add the username, his/her sent and received messages to your records.
If person with the given username already exists ignore the line.
"Message={sender}={receiver}":
Check if both usernames exist and if they do,
increase the sender’s sent messages by 1 and the receiver’s received messages by 1.
If anyone reaches the capacity (first check the sender),
he/she should be removed from the record and you should print the following message:
"{username} reached the capacity!"
"Empty={username}":
Delete all records of the given user, if he exists. If "All" is given as username - delete all records you have.
In the end, you have to print the count of users,
each person with his/her messages (the count of both sent and received)
sorted in descending order by the received messages and then by their username
in ascending order in the following format:
Users count: {count}
{username} - {messages}
{username} - {messages}
Input
On the first line, you will receive the capacity - an integer number in the range [1-10000].
You will be receiving lines until you receive the "Statistics" command.
The initial messages (sent and received) will always be below the capacity.
The input will always be valid.
Output
Print the appropriate message after the "Message" command, if someone reaches the capacity.
Print the users with their messages in the format described above.


Examples:
Input:
10
Add=Mark=5=4
Add=Clark=3=5
Add=Berg=9=0
Add=Kevin=0=0
Message=Berg=Kevin
Statistics

Output:
Berg reached the capacity!
Users count: 3
Clark - 8
Mark - 9
Kevin - 1

Comments:
First, we receive the capacity (10). Then we start receiving commands. The first four commands are for adding new users,
so we do it. Then we have the command “Message=Berg=Kevin” and Berg reached the capacity, so we remove him,
but Kevin has only his received messages incremented. When we receive the “Statistics” command,
we print the output as described above.

Input:
20
Add=Mark=3=9
Add=Berry=5=5
Add=Clark=4=0
Empty=Berry
Add=Blake=9=3
Add=Michael=3=9
Add=Amy=9=9
Message=Blake=Amy
Message=Michael=Amy
Statistics

Output:
Amy reached the capacity!
Users count: 4
Mark - 12
Michael - 13
Blake - 13
Clark - 4

Input:
12
Add=Bonnie=3=5
Add=Johny=4=4
Empty=All
Add=Bonnie=3=3
Statistics

Output:
Users count: 1
Bonnie - 6
"""

# This is the solution from in class. ... Done the worst way, but still ... correct:
"""
capacity = int(input())

users = []

command = input()
while command != "Statistics":

    commands_list = command.split("=")
    current_command = commands_list[0]

    if current_command == "Add":
        username = commands_list[1]
        sent = int(commands_list[2])
        received = int(commands_list[3])
        user = {"name": username, "sent": sent, "received": received}
        found = False
        for user_in_list in users:
            if user_in_list["name"] == username:
                found = True
        if not found:
            users.append(user)

    elif current_command == "Message":
        sender = commands_list[1]
        sender_found = False
        receiver = commands_list[2]
        receiver_found = False
        sender_dict = {}
        receiver_dict = {}
        for user_in_list in users:
            if user_in_list["name"] == sender:
                sender_found = True
                sender_dict = user_in_list
            if user_in_list["name"] == receiver:
                receiver_found = True
                receiver_dict = user_in_list
        if sender_found and receiver_found:
            sender_dict["sent"] += 1
            if sender_dict["sent"] + sender_dict["received"] >= capacity:
                print(f"{sender} reached the capacity!")
                users.remove(sender_dict)
            receiver_dict["received"] += 1
            if receiver_dict["sent"] + receiver_dict["received"] >= capacity:
                print(f"{receiver} reached the capacity!")
                users.remove(receiver_dict)

    elif current_command == "Empty":
        username = commands_list[1]
        if username == "All":
            users.clear()
        else:
            for user_in_list in users:
                if user_in_list["name"] == username:
                    users.remove(user_in_list)
                    break

    command = input()

print(f"Users count: {len(users)}")
sorted_list = sorted(users, key=lambda x: (-x["received"], x["name"]))

for user in sorted_list:
    print(f"{user['name']} - {(user['received'] + user['sent'])}")
"""

# Tis is the initial solution in which I have used the normal way with Dictionary
"""
capacity = int(input())

users = {}

while True:
    command = input().split("=")
    if command[0] == "Statistics":
        break

    elif command[0] == "Add":
        username = command[1]
        send = int(command[2])
        received = int(command[3])
        if username not in users:
            users[username] = [send, received]

    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender][0] += 1
            users[receiver][1] += 1
            if sum(users[sender]) >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]
            if sum(users[receiver]) >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif command[0] == "Empty":
        user_or_all = command[1]
        if user_or_all == "All":
            users.clear()
        elif user_or_all in users:
            del users[user_or_all]

print(f"Users count: {len(users)}")

for user, messages in sorted(users.items(), key=lambda x: (-(x[1][1]), x[0])):
    print(f"{user} - {sum(messages)}")
"""

# And this is the solution done with Object/Classes:
class User:
    max_messages = 0
    all = []

    def __init__(self, name: str, sent: int, received: int):
        self.name = name
        self.sent = sent
        self.received = received
        self.count_all_messages = sent + received

    @classmethod
    def is_present(cls, name_to_check):
        for user in User.all:
            if user.name == name_to_check:
                return True
        return False

    @classmethod
    def add(cls, name_to_add: str, sent_to_add: int, received_to_add: int):
        if not User.is_present(name_to_add):
            User.all.append(User(name=name_to_add, sent=sent_to_add, received=received_to_add))

    @classmethod
    def message(cls, sender: str, receiver:str):
        if User.is_present(sender) and User.is_present(receiver):
            for user in User.all:
                if user.name == sender:
                    user.sent += 1
                    user.count_all_messages += 1
                elif user.name == receiver:
                    user.received += 1
                    user.count_all_messages += 1
            User.check_capacity(sender)
            User.check_capacity(receiver)

    @classmethod
    def check_capacity(cls, name_to_check: str):
        for user in User.all:
            if user.name == name_to_check:
                if user.count_all_messages >= User.max_messages:
                    print(f"{user.name} reached the capacity!")
                    User.all.remove(user)

    @classmethod
    def empty(cls, name_or_all: str):
        if name_or_all == "All":
            User.all.clear()
        else:
            for user in User.all:
                if user.name == name_or_all:
                    User.all.remove(user)

    @classmethod
    def print_all(cls):
        print(f"Users count: {len(User.all)}")
        for user in sorted(User.all, key=lambda x: (-x.received, x.name)):
            print(f"{user.name} - {user.count_all_messages}")
        exit(0)


def run():
    User.max_messages = int(input())
    while True:
        command = input().split("=")
        if command[0] == "Statistics":
            print(User.print_all())
        elif command[0] == "Add":
            User.add(name_to_add=command[1], sent_to_add=int(command[2]), received_to_add=int(command[3]))
        elif command[0] == "Message":
            User.message(sender=command[1], receiver=command[2])
        elif command[0] == "Empty":
            User.empty(name_or_all=command[1])



if __name__ == '__main__':
    run()
