"""
Simple Operations and Calculations - More Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1642#0

09. Weather Forecast - Part 2

Условие:
Напишете програма, която при въведени градуси (реално число) принтира какво е времето,
като имате предвид следната таблица:
Градуси	Време
26.00 - 35.00	Hot
20.1 - 25.9	Warm
15.00 - 20.00	Mild
12.00 - 14.9	Cool
5.00 - 11.9	Cold
Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".
Примерен вход и изход
Вход	Изход
16.5	Mild
8	Cold
22.4	Warm
26	Hot
0	unknown
Насоки: потърсете информация за серии от проверки.
"""

g = float(input())
if g >= 26.00 and g <= 35.00:
    print("Hot")
elif g >= 20.1 and g <= 25.9:
    print("Warm")
elif g >= 15.00 and g <= 20.00:
    print("Mild")
elif g >= 12.00 and g <= 14.9:
    print("Cool")
elif g >= 5.00 and g <= 11.9:
    print("Cold")
else:
    print("unknown")