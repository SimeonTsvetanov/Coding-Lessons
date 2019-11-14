"""
Programming Fundamentals Mid Exam - 30 June 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1683#0

SUPyF2 P.-Mid-Exam/30 June 2019/2. - Giftbox Coverage

Problem:
Create a program that calculates what percentage you can cover of a 6-sided gift box (all sides are equal and square).
First, you will receive the size of a side. Also, you will receive the sheets of paper you have.
Last, you will receive how much area covers a single sheet of paper.
First, you need to calculate the area of the gift box.
Then you have to calculate how much area you can cover with the paper available.
Keep in mind that every third sheet covers only 25% of the usual area.
You have to calculate what percentage of the gift box you’ve covered. Percentage can exceed 100%!
In the end, print the percentage of the area covered, formatted to the 2nd decimal place, in the following format:
"You can cover {percentage}% of the box."
Input
•	On the 1st line you will receive the size of a side – a real number in the range [0.0…50.0]
•	On the 2rd line you will receive the number of sheets of paper – an integer number in the range [0…1000]
•	On the 3th line you will receive the area a single sheet of paper covers – a real number in the range[0.0…50.0]
•	The input will always be in the right format.
Output
•	In the end print the percentage of the area covered formatted to the
    2nd decimal place in the format described above.
Constraints
•	Percentage can be over 100%.
•	All numbers are centimeters.

Examples:
Input:
5
30
4

Output:
You can cover 60.00% of the box.

Comments:
The size of a side is 5. We have 6 sides, so the area is 5 * 5 * 6 = 150.
20 of sheets will cover 4 centimeters and 10 – 1 cm. The total area covered is 90, which is 60% of the total area.

Input:
2.5
32
4.25

Output:
You can cover 277.67% of the box.
"""
import math
size_of_a_side = float(input())
sheets_of_paper = int(input())
area_single_sheet = float(input())

total_area = size_of_a_side * size_of_a_side * 6
third_sheets = math.floor(sheets_of_paper / 3)
sheets_area = (sheets_of_paper - (third_sheets * 0.75)) * area_single_sheet
percentage = sheets_area * 100 / total_area

print(f"You can cover {percentage:.2f}% of the box.")
