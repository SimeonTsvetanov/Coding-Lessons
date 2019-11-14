"""
Simple Operations and Calculations - More Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1642#0

08. Weather Forecast

Условие:
Напишете програма, която познава дали е топло или студено навън.
От конзолата се чете един ред – текст, който подсказва какво е времето.
При въвеждане на "sunny" трябва да се отпечата "It's warm outside!".
Във всички останали случаи трябва да се отпечата "It's cold outside!".
Примерен вход и изход
Вход	Изход
sunny	It's warm outside!
cloudy	It's cold outside!
snowy	It's cold outside!
Насоки: потърсете информация за if-else конструкцията.
"""

weather = input()
if weather == "sunny":
    print("It's warm outside!")
if weather == "cloudy":
    print("It's cold outside!")
if weather == "snowy":
    print("It's cold outside!")
