"""
Programming Fundamentals Mid Exam - 2 November 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/1862/Programming-Fundamentals-Mid-Exam-2-November-2019-Group-2

SUPyF2 P.-Mid-Exam/2 November 2019/2. - Friends List Maintenance

Problem:
Our player is having trouble with his friend list and some guys are disappearing without a reason so he asks you to
create a program that will figure out what is going on and at the end will bring him a report.
On the first line you will receive all his friends separated by ", ".
On the next lines until the "Report" command you will receive commands. The commands could be:
•	Blacklist {name}
•	Find the name in the friend list and change it to "Blacklisted" and print on the console:
•	"{name} was blacklisted."
•	If the name is not in the friend list print:
•	"{name} was not found."
•	Error {index}
•	Check if the username at the given index is not "Blacklisted" or "Lost". If it isn't,
change the username to "Lost" and print on the console:
•	"{name} was lost due to an error."
•	Change {index} {newName}
•	Check if the user at index position is in range of the array. If he is,
change the current username with the new one and print on console:
•	"{currentName} changed his username to {newName}."
After you receive "Report" print on the console the count of blacklisted names,
the count of lost names, and the friend list separated by a single space.
Input
•	The first input line will contain the usernames that need to be stored.
•	On the next input lines until "Report" you will receive commands.
Output
•	The output should be in the following format:
•	"Blacklisted names: {blacklistedNamesCount}"
•	"Lost names: {lostNamesCount}"
•	"{name1} {name2} .. {nameN}"
Examples:

Input:
Mike, John, Eddie
Blacklist Mike
Error 0
Error 1
Change 2 Mike123
Report

Output:
Mike was blacklisted.
John was lost due to an error.
Eddie changed his username to Mike123.
Blacklisted names: 1
Lost names: 1
Blacklisted Lost Mike123

Comments:
On the first line are the names from the friendlist that need to be stored in an array.
After that the commands start to flow in. The first command finds Mike and blacklists him: "Mike was blacklisted."
After that "Error 0" failed because the name is already blacklisted and we do nothing.
"Error 1": John is replaced with "Lost" and the messange is sent to the console: "John was lost due to an error."
After that Mike changes his username to Mike123:  "Eddie changed his username to Mike123".
And the report is asked for so the program ends with the shown output.

Input:
Mike, John, Eddie, William
Error 3
Error 3
Change 0 Mike123
Blacklist Eddie
Report

Output:
William was lost due to an error.
Mike changed his username to Mike123.
Eddie was blacklisted.
Blacklisted names: 1
Lost names: 1
Mike123 John Blacklisted Lost
"""
all_friends = input().split(", ")

while True:
    command = input().split()
    if command[0] == "Report":
        break

    elif command[0] == "Blacklist":
        name = command[1]
        if name not in all_friends:
            print(f"{name} was not found.")
        else:
            index_name = all_friends.index(name)
            all_friends[index_name] = "Blacklisted"
            print(f"{name} was blacklisted.")

    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(all_friends):
            if all_friends[index] != "Blacklisted" and all_friends[index] != "Lost":
                name = all_friends[index]
                all_friends[index] = "Lost"
                print(f"{name} was lost due to an error.")

    elif command[0] == "Change":
        index, new_name = int(command[1]), command[2]
        if 0 <= index < len(all_friends):
            current_name = all_friends[index]
            all_friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")


print(f"Blacklisted names: {len([name for name in all_friends if name == 'Blacklisted'])}")
print(f"Lost names: {len([name for name in all_friends if name == 'Lost'])}")
print(*all_friends)

