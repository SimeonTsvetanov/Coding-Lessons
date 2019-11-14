"""
Simple Operations and Calculations - Lab
06. Circle Area and Perimeter
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1011#2
Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг /
окръжност с радиус r, като форматирате изхода до втория знак след десетичната запетая.
"""
import math

r = float(input())

a = math.pi * (r * r)
c = 2 * math.pi * r

print(f"{a:.2f}")
print(f"{c:.2f}")


