courses = {}

while True:
    command = input().split(' -> ')
    if command[0] == "End":
        break
    course_name, student_name = command
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)


for course_name, registered_students in courses.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")


