"""
Data Types and Variables - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1722#9

SUPyF2 D.Types and Vars Exercise - 10. Gladiator Expenses (not included in final score)

Problem:
As a gladiator, Petar has to repair his broken equipment when he loses a fight.
His equipment consists of helmet, sword, shield and armor. You will receive the Petar`s lost fights count.
Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also brakes.
Every second time, when his shield brakes, his armor also needs to be repaired.
You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.
Input / Constraints
You will receive 5 parameters to your function:
•	First parameter – lost fights count – integer in the range [0, 1000].
•	Second parameter – helmet price - floating point number in range [0, 1000].
•	Third parameter – sword price - floating point number in range [0, 1000].
•	Fourth parameter – shield price - floating point number in range [0, 1000].
•	Fifth parameter – armor price - floating point number in range [0, 1000].

Output:
•	As output you must print Petar`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
•	Allowed working time / memory: 100ms / 16MB.

Examples:
Input:
7
2
3
4
5
Output:
Gladiator expenses: 16.00 aureus
Comment:
Trashed helmet -> 3 times
Trashed sword -> 2 times
Trashed shield -> 1 time
Total: 6 + 6 + 4 = 16.00 aureus;

Input:
23
12.50
21.50
40
200
Output:
Gladiator expenses: 608.00 aureus
"""
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shield_count = 0

total_price = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        total_price += helmet_price
    if fight % 3 == 0:
        total_price += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        total_price += shield_price
        broken_shield_count += 1
        if broken_shield_count % 2 == 0:
            total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")
