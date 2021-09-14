"""
Dictionaries and Functional Programming
Проверка: https://judge.softuni.bg/Contests/Practice/Index/945#6

SUPyF Dictionaries - 07. User Logins

Problem:
Write a program that receives a list of username-password pairs in the format “{username} -> {password}”.
If there’s already a user with that username, replace their password. After you receive the command “login”,
login requests start coming in, using the same format. Your task is to print the status of user login,
using different messages as per the conditions below:
- If the password matches with the user’s password, print “{username}: logged in successfully”.
- If the user doesn’t exist, or the password doesn’t match the user, print “{username}: login failed”.
When you receive the command “end”, print the count of unsuccessful login attempts, using the format
“unsuccessful login attempts: {count}”.
Examples:
INPUT: <<<
walter_white58 -> iamthedanger
krazy_8 -> ese
jesseABQ -> bword
login
krazy_8 -> ese
krazy_8 -> ese
jesse -> bword
jesseabq -> bword
walter_white58 -> IAmTheDanger
walter_white58 -> iamthedanger
end

OUTPUT: >>>
krazy_8: logged in successfully
krazy_8: logged in successfully
jesse: login failed
jesseabq: login failed
walter_white58: login failed
walter_white58: logged in successfully
unsuccessful login attempts: 3
"""
name_pass = {}

counter = 0

while True:
    command = [item for item in input().split(" -> ")]
    if "login" in command:
        break
    name_pass[command[0]] = command[1]
while True:
    command = [item for item in input().split(" -> ")]
    if "end" in command:
        break
    if command[0] in name_pass and name_pass.__getitem__(command[0]) == command[1]:
        print(f"{command[0]}: logged in successfully")
    else:
        print(f"{command[0]}: login failed")
        counter += 1

print(f"unsuccessful login attempts: {counter}")


def another_solution():
    users = {}
    unsuccessful_login_attempts = 0

    while True:
        in_command = input().split(" -> ")
        if in_command[0] == "login":
            break
        in_name, in_password = in_command[0], in_command[1]
        users[in_name] = in_password

    while True:
        command = input().split(" -> ")
        if command[0] == "end":
            print(f"unsuccessful login attempts: {unsuccessful_login_attempts}")
            break
        username, password = command[0], command[1]
        if username in users.keys() and password == users[username]:
            print(f"{username}: logged in successfully")
        else:
            print(f"{username}: login failed")
            unsuccessful_login_attempts += 1


# another_solution()
