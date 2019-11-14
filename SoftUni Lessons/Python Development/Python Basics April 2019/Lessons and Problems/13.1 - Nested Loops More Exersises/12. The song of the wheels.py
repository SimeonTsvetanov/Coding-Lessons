m = int(input())

magic_password = None
counter = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if (a * b) + (c * d) == m:
                        print(f"{a}{b}{c}{d}", end=" ")
                        counter += 1
                        if counter == 4:
                            magic_password = str(a)+str(b)+str(c)+str(d)
print()
if counter >= 4:
    print(f"Password: {int(magic_password)}")
else:
    print(f"No!")










