"""
Functions and Debugging
Проверка: https://judge.softuni.bg/Contests/Compete/Index/922#4

05. Calculate Triangle Area

Условие:
Create a function that calculates and returns the area of a triangle by given base and height.
Use a general formatting with 12 digits after the decimal point (e.g. {area:.12g})

Examples
Input:
3
4
Output:
6

Hints
1.	After reading the input
2.	Create a function that calculates the area.
3.	Invoke the function in the main and save the return value in a new variable.
"""


def triangle_area(b, h):
    area = b * h / 2
    return f"{area:.12g}"


# Тук използвам принта за взимане на данни от конзилата и едновременно да принтира резултата от функцията по-горе.
# Друг вар. е да се вика с променлива, която да съдържа името на функцията с 2та инпута и после да принтираме тази
# променлива, когато си решим :)

print(triangle_area(float(input()), float(input())))











