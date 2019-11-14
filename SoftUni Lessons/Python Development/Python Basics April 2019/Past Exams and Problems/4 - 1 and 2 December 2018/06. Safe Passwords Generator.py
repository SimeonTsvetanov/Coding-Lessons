a = int(input())
b = int(input())
max_count = int(input())

A = 35
B = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        if max_count == 0:
            break
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        max_count -= 1
