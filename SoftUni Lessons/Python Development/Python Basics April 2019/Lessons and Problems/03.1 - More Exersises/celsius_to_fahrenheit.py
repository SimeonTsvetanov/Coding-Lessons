"""
Simple Operations and Calculations - More Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1642#0

03. Celsius to Fahrenheit

Условие:
Напишете програма, която чете градуси по скалата на Целзий (°C) и ги преобразува
до градуси по скалата на Фаренхайт (°F).
Потърсете в Интернет подходяща формула, с която да извършите изчисленията.
Форматирате изхода до втория знак след десетичната запетая.
"""

celsius = float(input())

fahrenheit = (celsius * 1.8) + 32

print(f"{fahrenheit:.2f}")
