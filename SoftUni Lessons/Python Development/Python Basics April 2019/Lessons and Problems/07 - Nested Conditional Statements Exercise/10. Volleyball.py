import math

y = input()
p = int(input())
h = int(input())

g = (((48 - h) * 3 / 4) + h) + (p * (2 / 3))

if y == "leap":
    g += g * 0.15

print(f"{math.floor(g)}")

