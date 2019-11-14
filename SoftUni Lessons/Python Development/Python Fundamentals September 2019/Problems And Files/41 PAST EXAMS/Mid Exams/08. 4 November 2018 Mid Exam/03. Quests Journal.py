"""
Technology Fundamentals Mid Exam - 4 November 2018
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1316#2

SUPyF2 P.-Mid-Exam/4 November 2018 - 03. Quests Journal

As a young adventurer, you start new quest every day, until you retire.
Input / Constraints
You start your adventurer path, receiving a journal with some beginner quests, separated with ', ' (comma and space).
After that, until receiving "Retire!" you will be receiving different commands.
Commands:
•	"Start - {quest}" – Receiving this command, you should add the given quest in your journal.
If the quest already exists, you should skip this line.
•	"Complete - {quest}" – You should remove the quest from your journal, if it exists.
•	"Side Quest - {quest}:{sideQuest}" – You should check if the quest exists, if so,
    add the side quest after the quest. Note that you shouldn`t add the sideQuest if it already exists.
•	"Renew – {quest}" – If the given quest exists, you should change its position and put it last in your journal.
Output
After receiving "Retire!" print the quests in the journal, separated by ", " (comma and space).

Examples:
Input                               Output:
Hello World, For loop, If else      Hello World, If else, While loop
Start - While loop
Complete - For loop
Retire!

Input:                              Output:
Hello World, If else                If else, Switch, Hello World
Complete - Homework
Side Quest - If else:Switch
Renew - Hello World
Retire!
"""
quests = input().split(", ")

while True:
    command = input().split(" - ")
    if command[0] == "Retire!":
        print(", ".join(quests))
        break
    elif command[0] == "Start":
        quest = command[1]
        if quest not in quests:
            quests.append(quest)
    elif command[0] == "Complete":
        quest = command[1]
        if quest in quests:
            quests.remove(quest)
    elif command[0] == "Side Quest":
        quest, side_quest = command[1].split(":")
        if side_quest not in quests and quest in quests:
            quests.insert((quests.index(quest) + 1), side_quest)
    elif command[0] == "Renew":
        quest = command[1]
        if quest in quests:
            quests.remove(quest)
            quests.append(quest)
