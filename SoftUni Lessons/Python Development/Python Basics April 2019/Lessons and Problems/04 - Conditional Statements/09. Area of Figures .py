"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

09. Area of Figures

Условие:
Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle):
-Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
-Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
-Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
-Ако фигурата е триъгълник, на следващите два реда четат две числа - дължината на страната му и
дължината на височината към нея.
Резултатът да се закръгли до 3 цифри след десетичната точка.
"""

import math
figure = input()

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == "circle":
    radius = float(input())
    area = math.pi * (radius * radius)
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * (height / 2)

print(f"{area:.3f}")
