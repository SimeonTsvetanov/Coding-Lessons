"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1578#0

SUPyF Exam Preparation 2 - 01. Date_Estimation

Problem:
Today is your exam. It’s 26th of August 2018. you will be given a single date in format year-month-day.
You should estimate if the date has passed regarding to the date mention above (2018-08-26),
if it is not or if it is today. If it is not you should print how many days are left till that date.
Note that the current day stills count!
Date Format:
yyyy-mm-dd
Output
The output should be printed on the console.
If the date has passed you should print the following output:
•	"Passed"
If the day is today:
"Today date"
If the date is future:
•	"{number of days} days"
Examples:
Input:
2018-08-20
Output:
Passed

Input:
2021-08-26
Output:
1097 days left
"""

from datetime import date
year, month, day = (int(item) for item in input().split("-"))
delta = date(2018, 8, 26) - date(year, month, day)

if delta.days == 0:
    print("Today date")
elif delta.days > 0:
    print("Passed")
else:
    print(f"{abs(delta.days) + 1} days left")
