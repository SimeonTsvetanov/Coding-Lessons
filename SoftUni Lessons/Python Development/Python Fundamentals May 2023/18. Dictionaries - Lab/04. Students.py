students = []

while True:
    command = input().split(':')
    if len(command) == 1:
        [print(f"{s['name']} - {s['number']}") for s in students if s['course'] == command[0]]
        break
    name = command[0]
    number = command[1]
    course = ' '.join(command[2:]).replace(' ', '_')
    students.append({'name': name, 'number': number, 'course': course})
