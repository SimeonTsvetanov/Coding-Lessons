"""
Simple Operations and Calculations - Exercise
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1160#0

03. 2D Rectangle Area

Условие:
Правоъгълник е зададен с координатите на два от своите срещуположни ъгъла (x1, y1) – (x2, y2).
Да се пресметнат площта и периметъра му.
Входът се чете от конзолата. Числата x1, y1, x2 и y2 са дадени по едно на ред.
Изходът се извежда на конзолата и трябва да съдържа два реда с по една число на всеки от тях – лицето и периметъра.
Резултатът да се форматира до 2 знака след запетаята.
"""

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1 - x2)
width = abs(y1 - y2)

area = length * width
perimeter = 2 * (length + width)

print(f"{area:.2f}")
print(f"{perimeter:.2f}")
