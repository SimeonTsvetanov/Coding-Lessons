# You will receive two lines of input:

# a list of employees' happiness as a string of numbers separated by a single space:
employees_happiness = [int(happy) for happy in input().split(' ')]
# a happiness improvement factor (single number):
factor = int(input())

# Your task is to find out if the employees are generally happy in their office.

# First, multiply each employee's happiness by the factor:
employees_happiness = [happy * factor for happy in employees_happiness]

# Then, print one of the following lines:

# If half or more of the employees have happiness greater than or equal to the average:
average_happiness = sum(employees_happiness) / len(employees_happiness)
count_happy_people = len([happy for happy in employees_happiness if happy >= average_happiness])

# If happy:
if count_happy_people >= len(employees_happiness) / 2:
    print(f"Score: {count_happy_people}/{len(employees_happiness)}. Employees are happy!")
# Otherwise:
else:
    print(f"Score: {count_happy_people}/{len(employees_happiness)}. Employees are not happy!")
