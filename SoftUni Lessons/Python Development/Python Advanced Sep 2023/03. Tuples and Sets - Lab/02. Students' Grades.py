students = {}

for _ in range(int(input())):
    command = input().split(' ')
    name = command[0]
    grade = float(command[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    print(f"{name} -> {' '.join([str(f'{g:.2f}') for g in grades])} (avg: {(sum(grades) / len(grades)):.2f})")
