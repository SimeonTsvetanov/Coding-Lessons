names = []
for _ in range(int(input())):
    name = input()
    if name not in names:
        names.append(name)

for name in names:
    print(name)
