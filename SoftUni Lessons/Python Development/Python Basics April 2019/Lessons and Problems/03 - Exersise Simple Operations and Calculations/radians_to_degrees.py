"""
Simple Operations and Calculations - Exercise
02. Radians to Degrees

Проверка: https://judge.softuni.bg/Contests/Compete/Index/1160#0
Условие:
Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg).
Закръглете резултата до най-близкото цяло число.
Използвайте формулата: градус = радиан * 180 / π.
Числото π в Python може да достъпите чрез модула math. За да ползвате функционалността му,
първо трябва да импортнете модула.
"""

import math
r = float(input())
g = r * 180 / math.pi

print(round(g))
