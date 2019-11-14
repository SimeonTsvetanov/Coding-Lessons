"""
Programming Fundamentals Mid Exam - 2 November 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/1859/Programming-Fundamentals-Mid-Exam-2-November-2019-Group-1

SUPyF2 P.-Mid-Exam/2 November 2019/1. - Biscuits Factory

Problem:
Create a program that calculates how many biscuits your factory can make for a month (30 days) and the percentage
of production compared to another factory production.
First, you will receive the biscuits produced per day (per worker). After that, you will receive the count of the
workers in your factory. Last, you will receive the number of biscuits that the competing factory produces for 30 days.
You need to calculate the production of your factory for 30 days.
Then you have to calculate how much more or fewer biscuits you produce compared to the other factory (in percentage).
There will be no case where the factories will produce the same amount of biscuits.
Every third day the workers produce only 75% of the usual production.
Keep in mind that there can be only a whole biscuit after making calculations for each day –
format them to the lower number.
In the end, print the amount of biscuits produced for 30 days in the following format:
"You have produced {countBiscuits} biscuits for the past month."
Then print the percentage of the difference, formatted to the 2nd decimal place, in the following format:
If your production is bigger than the other factory:
"You produce {percentage} percent more biscuits."
If not:
 "You produce {percentage} percent less biscuits."

Input:
•	On the first line you will receive the amount of biscuits a worker produce a day –
    an integer number in the range [1…200]
•	On the second line you will receive the count of the workers in your factory –
    an integer number in the range [1…1000]
•	On the third line you will receive the amount of biscuits that the competing factory produces for 30 days –
    an integer number in the range[1…2000]
NOTE: The input will always be in the right format.

Output:
•	In the end print the amount of biscuits produced for 30 days and the percentage of the difference formatted
    to the 2nd decimal place in the format described above.

Constraints:
•	Percentage can be over 100%.
•	There will be no case where the factories will produce the same amount of biscuits.

Examples:

Input:      Output:
78          You have produced 17160 biscuits for the past month.
8           You produce 7.25 percent more biscuits.
16000

Comments:
-78 biscuits a day
-8 employees
-17160 biscuit production your factory
    (keep in mind every third day the workers produce only 75% of the usual production)
-17160 – 16000 = 1160 - difference between your and the other factory production
-1160/16000 * 100 = 7.25% more biscuits.

Input:      Output:
65          You have produced 21450 biscuits for the past month.
12          You produce 17.50 percent less biscuits.
26000

Comments:
-65 biscuits a day
-12 employees
-21450 biscuit production your factory
-26000 – 21450 = 4550 - difference between your and the other factory production
-4550/26000 * 100 = 17.50% more biscuits.
"""
import math
biscuits_per_day = int(input()) * int(input())
other_factory_production = int(input())
our_factory_production = 0


def percentage(part, whole):
    return f'{abs((100 * float(part)/float(whole))- 100):.2f}'


for day in range(1, 31):
    if day % 3 == 0:
        our_factory_production += math.floor(biscuits_per_day * 0.75)
    else:
        our_factory_production += biscuits_per_day

print(f"You have produced {our_factory_production} biscuits for the past month.")
if our_factory_production > other_factory_production:
    print(f"You produce {percentage(our_factory_production, other_factory_production)} percent more biscuits.")
else:
    print(f"You produce {percentage(our_factory_production, other_factory_production)} percent less biscuits.")
