"""
Programming Fundamentals Mid Exam - 2 November 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/1862/Programming-Fundamentals-Mid-Exam-2-November-2019-Group-2

SUPyF2 P.-Mid-Exam/2 November 2019/2. - Experience Gaining

Problem:
Write a program, that helps a player figure how many battles he will need to play in a battle video game,
in order to unlock the next tank in the line.
On the first line you will receive the amount of experience that is needed to unlock the tank.
On the second line you will receive the count of battles. On the next lines,
you will receive the experience the player can gain in every battle.
Calculate if he can unlock the tank. Keep in mind that he gets 15% more experience for every third battle and
10% less for every fifth battle. You also need to stop the program as soon as he collects the needed experience.
If he managed to gather the experience, print how many battles it took him in the following format:
•	"Player successfully collected his needed experience for {battleCount} battles."
If he was not able to do it, print the following message:
•	"Player was not able to collect the needed experience, {neededExperience} more needed."
Format the needed experience to the second decimal place.
Input
•	On the first line you will receive the needed experience amount –  a real number in the range [0.0….400000.0]
•	On the second line you will receive the count of battles – an integer number in the range
[0….500]
•	On the next lines you will receive the experience earned per battle – a real number in the range
[0.0….5000.0]
Output
•	If he managed to gather the experience:
•	"Player successfully collected his needed experience for {battleCount} battles."
•	If he was not able to do it:
•	"Player was not able to collect the needed experience, {neededExperience} more needed."
NOTE: Format the needed experience to the second decimal place.

Examples:

Input:      Output:
500         Player successfully collected his needed experience for 5 battles.
5
50
100
200
100
30

Comments:
The first line is the amount of the wanted experience.  – "500"
The second line is the expected battles for which he has to collect the experience.  – "5"
After that is the experience received for every battle:
50 + 100 + (200 + (200 * 15 %)) + 100 + (30 – (30 * 10 %)) = 507
So on the console is printed :
"Player successfully collected his needed experience for 5 battles."

Input:      Output:
500         Player was not able to collect the needed experience, 2.00 more needed.
5
50
100
200
100
20

Input:     Output:
400        Player successfully collected his needed experience for 4 battles.
5
50
100
200
100
20
"""
needed_experience = float(input())
battles_count = int(input())
current_experience = 0

managed = False

for battle in range(1, battles_count + 1):
    new_experience = float(input())
    current_experience += new_experience
    if battle % 3 == 0:
        current_experience += new_experience * 0.15
    if battle % 5 == 0:
        current_experience -= new_experience * 0.1
    if current_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        managed = True
        break

if not managed:
    print(f"Player was not able to collect the needed experience, "
          f"{(needed_experience - current_experience):.2f} more needed.")
