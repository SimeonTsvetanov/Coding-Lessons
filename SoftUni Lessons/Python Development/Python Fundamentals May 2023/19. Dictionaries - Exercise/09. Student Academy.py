students = {}

for _ in range(int(input())):
    name = input()
    score = float(input())
    if name not in students:
        students[name] = []
    students[name].append(score)

for student, scores in students.items():
    average_score = sum(scores) / len(scores)
    if average_score >= 4.5:
        print(f"{student} -> {average_score:.2f}")
