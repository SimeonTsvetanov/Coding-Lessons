"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/967#0

SUPyF Exam Preparation 1 - 01. Sino the Walker

Problem:
Sino is one of those people that lives in SoftUni. He leaves every now and then,
but when he leaves he always takes a different route, so he needs to know how much time it will take for him to go home.
Your job is to help him with the calculations.
You will receive the time that Sino leaves SoftUni, the steps taken and time for each step, in seconds.
You need to print the exact time that he will arrive at home in the format specified.
Input / Constraints
•	The first line will be the time Sino leaves SoftUni in the following format: HH:mm:ss
•	The second line will contain the number of steps that he needs to walk to his home.
    This number will be an integer in range [0…2,147,483,647]
•	On the final line you will receive the time in seconds for each step.
    This number will be an integer in range [0…2,147,483,647]
Output
•	Print the time of arrival at home in the following format:
o	Time Arrival: {hours}:{minutes}:{seconds}
•	If hours, minutes or seconds are a single digit number, add a zero in front.
•	If, for example, hours are equal to zero, print a 00 in their place. The same is true for minutes or seconds.
•	Time of day starts at 00:00:00 and ends at 23:59:59

Examples:

Input:
12:30:30
90
1

Output:
Time Arrival: 12:32:00

Input:
23:49:13
5424
2

Output:
Time Arrival: 02:50:01
"""

from datetime import datetime, timedelta

start_time = datetime.strptime(input(), "%H:%M:%S")
added_time = timedelta(seconds=(float(input()) * float(input())))
end_time = ((start_time + added_time).time())
print(f"Time Arrival: {end_time}")


# Another Option from different person, as mine will generate a problem with larger int's then the sys.max size:
"""
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
 
    return "%02d:%02d:%02d" % (hour, minutes, seconds)
 
 
if __name__ == '__main__':
 
    time = input()
    steps = int(input())
    seconds_step = int(input())
 
    h, m, s = time.split(':')
    sec = (int(h)*3600) + (int(m)*60) + int(s)
    sec_home = sec + (steps*seconds_step)
    print(f'Time Arrival: {convert(sec_home)}')
"""
