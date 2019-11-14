"""
Simple Operations and Calculations - More Exercises
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1642#0

04. Vegetable Market

Условие:
Градинар продавал реколтата от градината си на зеленчуковата борса.
Продава зеленчуци за N лева на килограм и плодове за M лева за килограм.
Напишете програма, която да пресмята приходите от реколтата в евро ( ако приемем, че едно евро е равно на 1.94лв).
Вход
От конзолата се четат 4 числа, по едно на ред:
Първи ред – Цена за килограм зеленчуци – число с плаваща запетая
Втори ред – Цена за килограм плодове – число с плаваща запетая
Трети ред – Общо килограми на зеленчуците – цяло число
Четвърти ред – Общо килограми на плодовете – цяло число
Ограничения: Всички числа ще са в интервала от 0.00 до 1000.00
Изход
Да се отпечата на конзолата едно число: приходите от всички плодове и зеленчуци в евро.
"""

price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = float(input())
total_kg_fruits = float(input())

total_vegetables = price_kg_vegetables * total_kg_vegetables
total_fruits = price_kg_fruits * total_kg_fruits

total_bgn = total_vegetables + total_fruits
total_euro = total_bgn / 1.94

print(f"{total_euro:.15n}")

