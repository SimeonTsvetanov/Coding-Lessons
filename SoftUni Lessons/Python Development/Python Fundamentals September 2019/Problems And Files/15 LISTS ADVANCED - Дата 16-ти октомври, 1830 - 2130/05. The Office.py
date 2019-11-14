"""
Lists Advanced - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1730#4

SUPyF2 Lists-Advanced-Lab - 05. The Office

Problem:
You will receive two lines of input: a list of employee's happiness as string
with numbers separated by a single space and a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office.
To do that you have to increase their happiness by multiplying the all the employee's happiness
(the numbers from the list) by the factor, filter the employees which happiness is greater than or equal
to the average in the new list and print the result
There are two types of output:
•	If the half or more of the employees have
happiness >= than the average: "Score: {happy_count}/{unhappy_count}. Employees are happy!"
•	Otherwise:
"Score: {happy_count}/{unhappy_count}. Employees are not happy!"

Examples:
Input:
1 2 3 4 2 1
3
Output:
Score 2/6. Employees are not happy!
Comments:
After the mapping:
3 6 9 12 6 3
After the filtration:
9 12
2/6 people are happy, so the overall happiness is bad

Input:
2 3 2 1 3 3
4
Output:
Score: 3/6. Employees are happy!
Comments:
Half of the people are happy, so the overall happiness is good
"""

employees = [int(i) for i in input().split()]
improvement_factor = int(input())
employees = [employee * improvement_factor for employee in employees]
filtered = [emp for emp in employees if emp >= (sum(employees) / len(employees))]
if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")


