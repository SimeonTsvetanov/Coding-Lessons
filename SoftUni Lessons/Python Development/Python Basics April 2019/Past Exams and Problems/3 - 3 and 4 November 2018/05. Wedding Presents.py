total_guests = int(input())
gifts_count = int(input())

a = 0
b = 0
v = 0
g = 0

for i in range(gifts_count):
    category = input()
    if category == "A":
        a += 1
    elif category == "B":
        b += 1
    elif category == "V":
        v += 1
    elif category == "G":
        g += 1

print(f"{(a / gifts_count * 100):.2f}%")
print(f"{(b / gifts_count * 100):.2f}%")
print(f"{(v / gifts_count * 100):.2f}%")
print(f"{(g / gifts_count * 100):.2f}%")
print(f"{(gifts_count / total_guests * 100):.2f}%")

