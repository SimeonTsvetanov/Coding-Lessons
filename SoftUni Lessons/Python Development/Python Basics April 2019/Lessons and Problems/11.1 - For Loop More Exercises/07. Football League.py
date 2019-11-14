stadium_capacity = int(input())
count_fens = int(input())

a = 0
b = 0
v = 0
g = 0

for i in range(count_fens):
    sector = input()
    if sector == "A":
        a += 1
    if sector == "B":
        b += 1
    if sector == "V":
        v += 1
    if sector == "G":
        g += 1

print(f"{(a / count_fens * 100):.2f}%")
print(f"{(b / count_fens * 100):.2f}%")
print(f"{(v / count_fens * 100):.2f}%")
print(f"{(g / count_fens * 100):.2f}%")
print(f"{(count_fens / stadium_capacity * 100):.2f}%")
