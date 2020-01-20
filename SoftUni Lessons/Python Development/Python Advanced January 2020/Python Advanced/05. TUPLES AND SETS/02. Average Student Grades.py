students = {}

for _ in range(int(input())):
    data = input().split()
    name = data[0]
    grade = float(data[1])

    if name not in students:
        students[name] = [grade]
    else:
        students[name] += [grade]

for student, grades in students.items():
    print(f"{student} -> ", end="")
    for grade in grades:
        print(f"{grade:.2f}", end=' ')
    print(f"(avg: {(sum(grades) / len(grades)):.2f})")
