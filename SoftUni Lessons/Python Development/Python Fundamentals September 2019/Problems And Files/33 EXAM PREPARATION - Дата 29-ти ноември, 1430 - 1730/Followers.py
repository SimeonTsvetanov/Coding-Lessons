"""
Exam Preparation Programming Fundamentals Final Exam Retake - 9 August 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1767#2
Name: Followers

Problem:
Now that Pesho has successfully created an account, he wants to connect with other users and gain as many followers,
likes and comments as possible.
Create a program that keeps information about Pesho's followers, likes and comments. Keep a record of the followers,
each with the likes and comments Pesho has received from them.
You will be receiving lines with commands until you receive the "Log out" command.  There are four possible commands:
•	"New follower: {username}":
o	Add the username, to your records (with 0 likes and 0 comments).
If person with the given username already exists ignore the line.
•	"Like: {username}: {count}":
o	If the username doesn't exist, add it to your records with the given count of likes.
o	If the username exist, increase the count of likes with the given count.
•	"Comment: {username}":
o	If the username doesn't exist, add it to your records with 1 comment.
o	If the username exists, increase the count of commens with 1.
•	"Blocked: {username}":
o	Delete all records of the given username. If it doesn’t exist, print:
 "{Username} doesn't exist."

In the end, you have to print the count of followers, each follower with his/her likes and comments
(the sum of likes and comments)
sorted in descending order by the likes and then by their username in ascending order in the following format:
{count} followers
{username}: {likes+comments}
{username}: {likes+comments}
...
Input
•	You will be receiving lines until you receive the "Log out" command.
•	The input will always be valid.
Output
•	Print the users with their likes in the format described above.
Examples:
Input:
New follower: gosho
Like: gosho: 5
Comment: gosho
New follower: gosho
New follower: tosho
Comment: gosho
Comment: tosho
Comment: pesho
Log out

Output:
3 followers
gosho: 7
pesho: 1
tosho: 1

Input:
Like: A: 3
Comment: A
New follower: B
Blocked: A
Comment: B
Like: C: 5
Like: D: 5
Log out

Output:
3 followers
C: 5
D: 5
B: 1
"""

# There are two solutions I've created for this problem:

# Solution number one is as intended using Dictionaries:
"""
followers = {}


def new_follower(username: str):
    global followers
    if username not in followers:
        followers[username] = [0, 0]


def like(username: str, count: int):
    global followers
    if username not in followers:
        followers[username] = [count, 0]
    elif username in followers:
        followers[username][0] += count


def comment(username: str):
    global followers
    if username not in followers:
        followers[username] = [0, 1]
    elif username in followers:
        followers[username][1] += 1


def blocked(username: str):
    global followers
    if username in followers:
        del followers[username]
    elif username not in followers:
        print(f"{username} doesn't exist.")


def sort_and_print():
    global followers
    print(f"{len(followers)} followers")
    for follower, values in sorted(followers.items(), key=lambda x: (-x[1][0], x[0])):
        print(f"{follower}: {sum(values)}")
    exit(0)


def run():
    while True:
        command = input().split(": ")

        if command[0] == "New follower":
            new_follower(username=command[1])

        elif command[0] == "Like":
            like(username=command[1], count=int(command[2]))

        elif command[0] == "Comment":
            comment(username=command[1])

        elif command[0] == "Blocked":
            blocked(username=command[1])

        elif command[0] == "Log out":
            sort_and_print()


if __name__ == '__main__':
    run()
"""

# And Solution number two is using Object/Classes and functions :):

followers = []


class Follower:
    def __init__(self, name: str, likes=0, comments=0):
        self.name = name
        self.likes = likes
        self.comments = comments


def new_follower(username: str):
    global followers
    follower_is_present = False
    for follower in followers:
        if follower.name == username:
            follower_is_present = True
    if not follower_is_present:
        followers += [Follower(name=username)]


def like(username: str, count: int):
    global followers
    follower_is_present = False
    for follower in followers:
        if follower.name == username:
            follower_is_present = True
            follower.likes += count
    if not follower_is_present:
        followers += [Follower(name=username, likes=count)]


def comment(username: str):
    global followers
    follower_is_present = False
    for follower in followers:
        if follower.name == username:
            follower_is_present = True
            follower.comments += 1
    if not follower_is_present:
        followers += [Follower(name=username, comments=1)]


def blocked(username: str):
    global followers
    follower_is_present = False
    for follower in followers:
        if follower.name == username:
            follower_is_present = True
            followers.remove(follower)
    if not follower_is_present:
        print(f"{username} doesn't exist.")


def sort_and_print():
    global followers
    print(f"{len(followers)} followers")
    for follower in sorted(followers, key=lambda x: (-x.likes, x.name)):
        print(f"{follower.name}: {follower.likes + follower.comments}")


def run():
    while True:
        command = input().split(": ")

        if command[0] == "New follower":
            new_follower(username=command[1])

        elif command[0] == "Like":
            like(username=command[1], count=int(command[2]))

        elif command[0] == "Comment":
            comment(username=command[1])

        elif command[0] == "Blocked":
            blocked(username=command[1])

        elif command[0] == "Log out":
            sort_and_print()
            break


if __name__ == '__main__':
    run()
