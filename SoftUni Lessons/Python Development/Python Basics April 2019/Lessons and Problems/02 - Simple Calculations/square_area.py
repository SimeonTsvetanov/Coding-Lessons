"""
Simple Operations and Calculations - Lab
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1011#2
03. Square Area
Напишете конзолна програма, която въвежда цяло число 'a' и пресмята лицето на квадрат със страна 'a'.
"""

side = float(input())
area = side * side
print(int(area))

# another way : area a ** 2
# another way : import math (place it on the top) and then :
# are = math.pow(a, 2)
