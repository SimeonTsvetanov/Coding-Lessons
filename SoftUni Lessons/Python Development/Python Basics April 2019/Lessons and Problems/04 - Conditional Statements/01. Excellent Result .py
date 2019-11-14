"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

01. Excellent Result

Условие:
Първата задача от тази тема е да се напише конзолна програма, която чете оценка (десетично число),
въведена от потребителя и отпечатва "Excellent!", ако оценката е 5.50 или по-висока.
"""

grade = float(input())
if grade >= 5.5:
    print("Excellent!")
