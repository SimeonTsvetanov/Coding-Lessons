"""
Simple Operations and Calculations - More Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1642#0

02. Triangle Area

Условие:
Напишете програма, която чете от конзолата страна и височина на триъгълник и пресмята неговото лице.
Използвайте формулата за лице на триъгълник: area = a * h / 2.
Форматирате изхода до втория знак след десетичната запетая.
"""

side = float(input())
height = float(input())

area = side * height / 2

print(f"{area:.2f}")
