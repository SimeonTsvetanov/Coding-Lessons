"""
Simple Operations and Calculations - Exercise
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1160#0

07. Alcohol Market

Условие:
Пешо решава да направи купон и отива до алкохолната борса за да купи бира, вино, ракия и уиски. Да се напише програма,
която пресмята колко пари са му необходими за да плати сметката, като знаете, че:
цената на ракията е на половина по-ниска от тази на уискито;
цената на виното е с 40% по-ниска от цената на ракията;
цената на бирата е с 80% по-ниска от цената на ракията.
Вход
От конзолата се четат 5 реда:
1.	Цена на уискито в лева – реално число;
2.	Количество на бирата в литри – реално число;
3.	Количество на виното в литри – реално число;
4.	Количество на ракията в литри – реално число;
5.	Количество на уискито в литри – реално число.
Изход
Да се отпечата на конзолата едно число:
парите, които са необходими на Пешо, форматирани до втория знак след десетичната запетая.
"""

whiskey_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
rakia_liters = float(input())
whiskey_liters = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price - (0.4 * rakia_price)
beer_price = rakia_price - (0.8 * rakia_price)

whiskey_total = whiskey_price * whiskey_liters
rakia_total = rakia_price * rakia_liters
wine_total = wine_price * wine_liters
beer_total = beer_price * beer_liters

total = whiskey_total + rakia_total + wine_total + beer_total
print(f"{total:.2f}")

