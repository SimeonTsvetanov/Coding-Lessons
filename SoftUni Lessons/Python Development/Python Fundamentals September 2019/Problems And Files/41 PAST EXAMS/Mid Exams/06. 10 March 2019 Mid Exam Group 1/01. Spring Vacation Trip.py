"""
Technology Fundamentals Mid Exam - 10 March 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1494#0

SUPyF2 P.-Mid-Exam/10 March 2019/1 - 01. Spring Vacation Trip

Problem:
A group of friends decide to go to a trip for a few days during spring vacation.
They have a certain budget. Your task is to calculate their expenses during the trip and find out if they are going
to have enough money to finish the vacation.
Create a program that calculates travelling expenses by entering the following information:
-	Days of the vacation
-	Budget - its for the whole group
-	The count of people
-	Fuel per kilometer – the price for fuel that their car consumes per kilometer
-	Food expenses per person
-	Hotel room price for one night – again, for one person
If the group is bigger than 10, they receive a 25% discount from the total hotel expenses.
Every day, they travel some distance and you have to calculate the expenses for the travelled kilometers.
Every third and fifth day, they have some additional expenses, which are 40% of the current value of the expenses.
Every seventh day, their expenses are reduced, because they withdraw (receive) a small amount of money –
you can calculate it by dividing the amount of the current expenses by the group of people.
If the expenses exceed the budget at some point, stop calculating and print the following message:
"Not enough money to continue the trip"
If the budget is enough:
"You have reached the destination. You have {money}$ budget left."
Print the result formatted 2 digits after the decimal separator.
Input / Constraints
•	On the 1st line, you are going to receive the days of the trip – an integer in the range [1…100]
•	On the 2nd line – the budget – a real number in the range [0.00 – 1000000.00]
•	On the 3rd line - the group of people – an integer in the rang [1 - 50]
•	On the 4th line – the price for fuel per kilometer – a real number [0.00 – 20.00]
•	On the 5th line – food expenses per person for a day – a real number [0.00 – 50.00]
•	On the 6th line – the price for a room for one night per person – a real number [0.00 – 1000.00]
•	On the next n lines – one for each of the days – the travelled distance in kilometers per day–
a real number in the range [0.00 - 1000]
Output
•	"Not enough money to continue the trip. You need {money}$ more." –
if the budget is not enough
•	"You have reached the destination. You have {money}$ budget left." – if it’s enough.
Print the result formatted 2 digits after the decimal separator.
Examples:
Input:
7
12000
5
1.5
10
20
512
318
202
154
222
108
123

Output:
You have reached the destination. You have 5083.48$ budget left.

Comments:
We receive the days of the vacation, the budget, the group, the consumed fuel per kilometer,
the food expenses and the price for a hotel room for one night. We must calclate the food expenses: 10 * 5 * 7 = 350
And the price for the hotel for all of the nights:
20 * 5 * 7 = 700
The curent expenses are 1050. For each day, we have to calculate the consumed fuel – {travelledDistance} * 1.5
On every 3rd  and 5th  day we add the additional expenses:
0.4 * {currentExpenses}
On every 7th day, they receive some money:
{currentExpense} / {groupOfPeople}
After we have added the fuel expenses for each day and made the other calculations,
the expenses have reached 8645.652. When we divide them by the group (5), the result is 1729.1304,
so we have to reduce the expenses by that sum. The expenses become 6916.5216. The budget is enough, so the result is:
"You have reached the destination. You have 5083.48$ budget left."

Input:
10
20500
11
1.2
8
13
100
150
500
400
600
130
300
350
200
300

Output:
Not enough money to continue the trip. You need 465.79$ more.
"""
days = int(input())
budget = float(input())
people = int(input())
price_km = float(input())

food_price = float(input()) * people * days
hotel_price = float(input()) * people * days

if people > 10:
    hotel_price -= hotel_price * 0.25

expenses = food_price + hotel_price

for day in range(1, days + 1):
    expenses += float(input()) * price_km
    if day % 3 == 0 or day % 5 == 0:
        expenses += expenses * 0.4
    if day % 7 == 0:
        expenses -= expenses / people
    if expenses > budget:
        print(f"Not enough money to continue the trip. You need {(expenses - budget):.2f}$ more.")
        break

if budget >= expenses:
    print(f"You have reached the destination. You have {(budget - expenses):.2f}$ budget left.")
