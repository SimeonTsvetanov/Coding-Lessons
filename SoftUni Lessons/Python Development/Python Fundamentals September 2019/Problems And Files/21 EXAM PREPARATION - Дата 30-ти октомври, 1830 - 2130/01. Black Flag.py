"""
Programming Fundamentals Mid Exam Retake - 6 August 2019
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1773#0

SUPyF2 P.-Mid-Exam/6 August 2019. - Black Flag

Problem:
Pirates are invading the sea and you're tasked to help them plunder
Create a program that checks if a target plunder is reached.
First you will receive how many days the pirating lasts.
Then you will receive how much the pirates plunder for a day.
Last you will receive the expected plunder at the end.
Calculate how much plunder the pirates manage to gather. Each day they gather plunder.
Keep in mind that every third day they attack more ships and they add
additional plunder to their total gain which is 50% of the daily plunder.
Every fifth day the pirates encounter a warship and after the battle they lose 30% of their total plunder.
If the gained plunder is more or equal to the target print the following:
"Ahoy! {totalPlunder} plunder gained."
If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."
Both numbers should be formatted to the 2nd decimal place.
Input:
•	On the 1st line you will receive the days of the plunder – an integer number in the range [0…100000]
•	On the 2nd line you will receive the daily plunder – an integer number in the range [0…50]
•	On the 3rd line you will receive the expected plunder – a real number in the range [0.0…10000.0]
Output:
•	 In the end print whether the plunder was successful or not following the format described above.
Examples:
Input:      Output:
5           Ahoy! 154.00 plunder gained.
40
100
Comments:
The days are 5 and the daily plunder is 40.
On the third day the total plunder is 120 and since it is a third day,
they gain an additional 50% from the daily plunder which adds up to 140.
On the fifth day the plunder is 220,
but they battle with a warship and lose 30% of the collected cargo and the total becomes 154.
That is more than the expected.

Input:      Output:
10          Collected only 36.29% of the plunder.
20
380
"""
# days = int(input())
# plunder_for_a_day = int(input())
# expected_plunder = int(input())
#
# total_plunder = 0
#
# for day in range(1, days + 1):
#     total_plunder += plunder_for_a_day
#     if day % 3 == 0:
#         total_plunder += plunder_for_a_day / 2
#     if day % 5 == 0:
#         total_plunder *= 0.7
#
# if total_plunder >= expected_plunder:
#     print(f"Ahoy! {total_plunder:.2f} plunder gained.")
# else:
#     print(f"Collected only {(100 * float(total_plunder) / float(expected_plunder)):.2f}% of the plunder.")
days = int(input())
daily_plunder = int(input())
target_plunder = float(input())

total_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= target_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(100 * (float(total_plunder) / float(target_plunder))):.2f}% of the plunder.")





























