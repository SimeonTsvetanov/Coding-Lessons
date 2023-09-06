n = int(input())
opened = 0
closed = 0

for i in range(n):
    line = input()
    if line == "(":
        opened += 1
        if (opened - closed) > 1:
            print("UNBALANCED")
            exit(0)
    elif line == ")":
        closed += 1
        if (opened - closed) != 0:
            print("UNBALANCED")
            exit(0)

if opened == closed:
    print("BALANCED")
else:
    print("UNBALANCED")