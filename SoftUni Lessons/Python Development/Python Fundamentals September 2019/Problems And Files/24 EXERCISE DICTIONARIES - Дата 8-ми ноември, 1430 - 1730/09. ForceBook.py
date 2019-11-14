"""
Dictionaries - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1737#8

SUPyF2 Dict-Exercise - 09. ForceBook (not included in final score)

Problem:
The force users are struggling to remember which side are the different forceUsers from,
because they switch them too often. So you are tasked to create a web application to manage their profiles.
You should store an information for every unique forceUser, registered in the application.
You will receive several input lines in one of the following formats:
{forceSide} | {forceUser}
{forceUser} -> {forceSide}
The forceUser and forceSide are strings, containing any character.
If you receive forceSide | forceUser, you should check if such forceUser already exists, and if not,
add him/her to the corresponding side.
If you receive a forceUser -> forceSide, you should check if there is such a forceUser already and if so,
change his/her side. If there is no such forceUser, add him/her to the corresponding forceSide,
treating the command as a new registered forceUser.
Then you should print on the console: "{forceUser} joins the {forceSide} side!"
You should end your program when you receive the command "Lumpawaroo".
At that point you should print each force side, ordered descending by forceUsers count,
than ordered by name. For each side print the forceUsers, ordered by name.
In case there are no forceUsers in a side, you shouldn`t print the side information.
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	The input ends, when you receive the command "Lumpawaroo".
Output
•	As output for each forceSide, ordered descending by forceUsers count, then by name,
you must print all the forceUsers, ordered by name alphabetically.
•	The output format is:
Side: {forceSide}, Members: {forceUsers.Count}
! {forceUser}
! {forceUser}
! {forceUser}
•	In case there are NO forceUsers, don`t print this side.
Examples:
Input:
Light | Gosho
Dark | Pesho
Lumpawaroo

Output:
Side: Dark, Members: 1
! Pesho
Side: Light, Members: 1
! Gosho

Comments:
We register Gosho in the Light side and Pesho in the Dark side.
After receiving "Lumpawaroo" we print both sides, ordered by membersCount and then by name.

Input;
Lighter | Royal
Darker | DCay
Ivan Ivanov -> Lighter
DCay -> Lighter
Lumpawaroo

Output:
Ivan Ivanov joins the Lighter side!
DCay joins the Lighter side!
Side: Lighter, Members: 3
! DCay
! Ivan Ivanov
! Royal

Comments:
Although Ivan Ivanov doesn`t have profile, we register him and add him to the Lighter side.
We remove DCay from Darker side and add him to Lighter side.
We print only Lighter side because Darker side has no members.
"""
sides = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    tokens = command.split(" | ")

    if len(tokens) == 2:
        side, user = tokens
        is_contained = False
        for key, value in sides.items():
            if user in value:
                is_contained = True
        if not is_contained:
            if side not in sides:
                sides[side] = []
            sides[side].append(user)

    else:
        tokens = command.split(" -> ")
        user, side = tokens

        for key, value in sides.items():
            if user in value:
                sides[key].remove(user)

        if side not in sides:
            sides[side] = []
        sides[side].append(user)
        print(f"{user} joins the {side} side!")

for side, users in sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(users) >= 1:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")
