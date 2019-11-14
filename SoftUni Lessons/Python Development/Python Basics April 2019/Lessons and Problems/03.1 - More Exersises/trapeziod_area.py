"""
Simple Operations and Calculations - More Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1642#0

01. Trapeziod Area

Условие:
Напишете програма, която чете от конзолата три числа b1, b2 и h
и пресмята лицето на трапец с основи b1 и b2 и височина h. Формулата за лице на трапец е (b1 + b2) * h / 2.
На фигурата по-долу е показан трапец със страни 8 и 13 и височина 7. Той има лице (8 + 13) * 7 / 2 = 73.5.
"""

b1 = float(input())
b2 = float(input())
h = float(input())

area = (b1 + b2) * h / 2
print(f"{area:.2f}")
