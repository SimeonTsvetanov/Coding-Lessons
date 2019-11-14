"""
Programming Fundamentals Mid Exam - 30 June 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1682#0

SUPyF2 P.-Mid-Exam/30 June 2019/1 - Distance Calculator

Problem:
Create a program that calculates what percentage you’ve travelled.
First, you will receive how many steps you’ve made.
Then, you will receive how long 1 step is in centimeters.
Last, you will receive the distance you need to travel in meters.
Then you have to calculate what distance you have travelled with the steps given.
Have in mind that every fifth step is 30% shorter than usual.
You have to calculate what percentage of the distance you’ve travelled.
In the end, print the percentage of the distance travelled, formatted to the 2nd decimal place, in the following format:
"You travelled {percentage}% of the distance!"
Input
•	On the 1st line you will receive the steps made – an integer number in the range [0…100000]
•	On the 2nd line you will receive the length of 1 step – a real number in the range [0.0…50.0]
•	On the 3rd line you will receive the distance you need to travel – an integer number in the range [0…100000]
Output
•	In the end print the percentage of the distance travelled
    formatted to the 2nd decimal place in the format described above.
Constraints
•	The input will always be in the right format.
•	Percentage can be over 100%.
 
Examples:
Input:      Output:
100         You travelled 188.00% of the distance!
2
1
Comments:
The length of a step is 2 centimeters.
Every fifth step will be 1.4 centimeters long.
20 shorter steps are made.
The distance that has to be travelled is 1 meter.
The distance travelled is 1.88 meters which is 188% of the distance that had to be travelled.

Input:      Output:
5000        You travelled 70.50% of the distance!
7.5
500
"""
steps = int(input())
step_in_cm = float(input())
distance = float(input())


def percentage(part, whole):
    return f"{(100 * float(part)/float(whole)):.2f}"


distance_traveled = 0
for step in range(1, steps + 1):
    if step % 5 == 0:
        distance_traveled += step_in_cm * 0.7
    else:
        distance_traveled += step_in_cm
distance_traveled_in_m = distance_traveled / 100

print(f"You travelled {percentage(distance_traveled_in_m, distance)}% of the distance!")
