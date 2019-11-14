a = int(input())
b = int(input())
max_counter = int(input())

A = 35
B = 64

for x in range(1, a + 1):
    if max_counter == 0:
        break
    for y in range(1, b + 1):
        if max_counter == 0:
            break
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        max_counter -= 1

