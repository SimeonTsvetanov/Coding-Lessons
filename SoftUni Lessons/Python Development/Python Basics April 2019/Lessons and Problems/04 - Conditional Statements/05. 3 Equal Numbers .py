"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

05. 3 Equal Numbers

Условие:
Да се въведат 3 числа и да се отпечата дали са еднакви (yes / no).
"""

num_1 = float(input())
num_2 = float(input())
num_3 = float(input())

if num_1 == num_2 and num_2 == num_3:
    print("yes")
else:
    print("no")

