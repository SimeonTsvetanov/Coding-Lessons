"""
Technology Fundamentals Mid Exam - 4 November 2018
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1316#0

SUPyF2 P.-Mid-Exam/4 November 2018 - 01. Party Profit

Problem:
As a young adventurer, you travel with your party around the world, seeking for gold and glory.
But you need to split the profit among your companions.
You will receive a party size. After that you receive the days of the adventure.
Every day, you are earning 50 coins, but you also spent 2 coin per companion for food.
Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.
Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion.
But if you have a motivational party the same day, you spent additional 2 coins per companion.
Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
You have to calculate how much coins gets each companion at the end of the adventure.
Input / Constraints
The input will consist of exactly 2 lines:
•	party size – integer in range [1…100]
•	days – integer in range [1…100]
Output
Print the following message: "{companionsCount} companions received {coins} coins each."
You cannot split a coin, so take the integral part (round down the coins to integer number).
Examples:
Input: Output:
3      3 companions received 90 coins each.
5

Input: Output:
15     3 companions received 90 coins each.
30
"""
import math

people = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        people -= 2
    if day % 15 == 0:
        people += 5

    coins += 50 - (2 * people)

    if day % 3 == 0:
        coins -= 3 * people
    if day % 5 == 0:
        coins += 20 * people
        if day % 3 == 0:
            coins -= 2 * people

print(f"{people} companions received {math.floor(coins / people)} coins each.")
