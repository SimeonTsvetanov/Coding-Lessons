"""
Technology Fundamentals Retake Mid Exam - 18 December 2018
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1395#1

SUPyF2 P.-Mid-Exam/18 December 2018 - 02. Santa's List

Problem:
Its Christmas time and Santa needs your help with creating the list of noisy kids.
Input
You will receive the initial list with noisy kids each of them separated with "&".
After that you will receive 4 types of commands until you receive "Finished!"
•	Bad {kidName} - adds a kid at the start of the list.  If the kid already exists skip this line.
•	Good {kidName} - removes the kid with the given name only if he exists in the list, otherwise skip this line.
•	Rename {oldName} {newName} – if the kid with the given old name exists change his name with the newer one.
If he doesn't exist skip this line.
•	Rearrange {kidName} - If the kid exists in the list remove him from his current position and
    add him at the end of the list.
Constraints
•	You won't receive duplicate names in the initial list
Output
Print the list of all noisy kids joined by ", ".
•	"{firstKid}, {secondKid}, …{nthKid}"

Examples:

Input:	                Output:
Peter&George&Mike       Joshua, George, Mike
Bad Joshua
Good Peter
Finished!

Input:	                                Output:
Joshua&Aaron&Walt&Dustin&William        Joshua, Paul, Dustin, William, Jon
Good Walt
Bad Jon
Rename Aaron Paul
Rearrange Jon
Rename Peter George
Finished!
"""
noisy_kids = input().split("&")

while True:
    command = input().split()
    if command[0] == "Finished!":
        print(", ".join(noisy_kids))
        break

    elif command[0] == "Bad":
        bad_name = command[1]
        if bad_name not in noisy_kids:
            noisy_kids.insert(0, bad_name)

    elif command[0] == "Good":
        good_kid = command[1]
        if good_kid in noisy_kids:
            noisy_kids.remove(good_kid)

    elif command[0] == "Rename":
        old_name, new_name = command[1], command[2]
        if old_name in noisy_kids:
            index_old_name = noisy_kids.index(old_name)
            noisy_kids[index_old_name] = new_name

    elif command[0] == "Rearrange":
        kid_name = command[1]
        if kid_name in noisy_kids:
            noisy_kids.remove(kid_name)
            noisy_kids.append(kid_name)
