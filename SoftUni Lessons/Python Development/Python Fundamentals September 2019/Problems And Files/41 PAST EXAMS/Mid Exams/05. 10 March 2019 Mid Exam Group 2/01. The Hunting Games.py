"""
Technology Fundamentals Mid Exam - 10 March 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1555#0

SUPyF2 P.-Mid-Exam/10 March 2019/2 - 01. The Hunting Games

Problem:
A group of friends have decided to participate in a game called "The Hunting Games".
The first stage of the game is to gather some supplies.
They have a list and your job is to help them follow it and make the needed calculations.
Write a program that calculates the needed provisions for a quest in the woods.
First you will receive the days of the adventure, the count of the players and the group’s energy.
Afterwards, you will receive the following provisions per day for one person:
	Water
	Food
The group calculates how many supplies they’d need for the adventure and take that much water and food.
Every day they chop wood and lose a certain amount of energy.
For each of the days, you are going to receive the energy loss from chopping wood.
The program should end If the energy reaches 0 or less.
Every second day they drink water,
which boosts their energy with 5% of their current energy and at the same time drops
their water supplies by 30% of their current water.
Every third day they eat, which reduces their food supplies by the following amount:
{currentFood} / {countOfPeople} and at the same time raises their group’s energy by 10%.
The chopping of wood, the drinking of water, and the eating happen in the order above.
If they have enough energy to finish the quest, print the following message:
"You are ready for the quest. You will be left with - {energyLevel} energy!"
If they run out of energy print the following message and the food and water they were left
with before they ran out of energy:
"You will run out of energy. You will be left with {food} food and {water} water."
Input / Constraints
•	On the 1st line, you are going to receive a number N - the days of the adventure – an integer in the range [1…100]
•	On the 2nd line – the count of players – an integer in the range [0 – 1000]
•	On the 3rd line - the group’s energy – a real number in the range [1 - 50000]
•	On the 4th line – water per day for one person – a real number [0.00 – 1000.00]
•	On the 5th line – food per day for one person – a real number [0.00 – 1000.00]
•	On the next N lines – one for each of the days – the amount of energy loss– a real number in the range [0.00 - 1000]
•	You will always have enough food and water.
Output
•	"You are ready for the quest. You will be left with - {energyLevel} energy!" –
if they have enough energy
"You will run out of energy. You will be left with {food} food and {water} water."
•	All of the real numbers should be formatted to the second digit after the decimal separator

Examples:
Input:      Output:
10          You are ready for the quest. You will be left with - 658.72 energy!
7
5035.5
11.3
7.2
942.3
500.57
520.68
540.87
505.99
630.3
784.20
321.21
456.8
330

Comments:
The days are 10 and the players are 7. The energy of the whole group is 5035.5.
We receive the water and food and we can calculate the needed amount of both for the whole quest:
10 * 7 * 11.3 – total water = 791
10 * 7 * 7.2 – total food = 504
Afterwards, for each of the days you have to calculate the energy loss.
On each day you receive energy loss and you have to subtract it. On the first day it is:
5035.5 – 942.3 = 4093.2
On every second day we add the energy boost from the drank water,
which is 5% of the current energy and subtract the amount from the total water.
The first time we reach a second day, the energy will become 3772.26 and the water will become 553.7.
The first time we reach a third day,
we have to boost the energy with 10% and reduce the food supplies and the energy will become - 3576.74 and the food 432.
Make all of the calculations and in the end, you must have 658.77 energy left and 132.94 water and 317.39 food left.
"""
days = int(input())
players = int(input())
energy = float(input())
water = days * players * float(input())
food = days * players * float(input())

for i in range(1, days + 1):
    energy -= float(input())

    if energy <= 0:
        break
    if i % 2 == 0:
        water *= 0.7
        energy *= 1.05
    if i % 3 == 0:
        food -= food / players
        energy *= 1.1
if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
