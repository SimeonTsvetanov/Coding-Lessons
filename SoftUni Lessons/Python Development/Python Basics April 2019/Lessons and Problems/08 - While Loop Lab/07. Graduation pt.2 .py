name = input()
total_grades = 0.0
class_count = 1
expel_count = 1

is_expelled = False

while class_count <= 12:
    grade = float(input())

    if grade >= 4.00:
        class_count += 1
        total_grades += grade
    else:
        expel_count += 1
    if expel_count == 2:
        is_expelled = True
        break

if is_expelled:
    print(f"{name} has been excluded at {class_count} grade")
else:
    print(f"{name} graduated. Average grade: {(total_grades / 12):.2f}")