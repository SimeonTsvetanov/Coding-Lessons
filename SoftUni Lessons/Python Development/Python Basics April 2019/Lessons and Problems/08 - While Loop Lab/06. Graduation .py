name = input()
grades = 1.0
total = 0.0

while grades <= 12:
    grade = float(input())
    if grade >= 4.00:
        total += grade
        grades += 1
average = total / 12
print(f"{name} graduated. Average grade: {average:.2f}")
