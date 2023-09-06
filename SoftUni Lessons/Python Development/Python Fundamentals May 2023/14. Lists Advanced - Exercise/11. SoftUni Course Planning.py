subject_list = input().split(", ")

next_command = input()

while next_command != "course start":
    next_command_list = next_command.split(":")
    command = next_command_list[0]
    title = next_command_list[1]
    exercise = title + "-Exercise"

    if command == "Add":
        if title not in subject_list:
            subject_list.append(title)

    elif command == "Insert":
        index = int(next_command_list[2])
        if index < len(subject_list):
            if title not in subject_list:
                subject_list.insert(index, title)

    elif command == "Remove":
        if title in subject_list:
            subject_list.remove(title)
            if exercise in subject_list:
                subject_list.remove(exercise)

    elif command == "Swap":
        title_1 = next_command_list[1]
        title_2 = next_command_list[2]
        exercise_two = title_2 + "-Exercise"
        if title_1 and title_2 in subject_list:
            index_1 = subject_list.index(title_1)
            index_2 = subject_list.index(title_2)
            if exercise in subject_list and exercise_two in subject_list:
                subject_list[index_1], subject_list[index_2] = \
                    subject_list[index_2], subject_list[index_1]
                subject_list.remove(exercise)
                subject_list.remove(exercise_two)
                subject_list.insert(index_2 + 1, exercise)
                subject_list.insert(index_1 + 1, exercise_two)
            elif exercise in subject_list:
                subject_list[index_1], subject_list[index_2], = subject_list[index_2], subject_list[index_1]
                subject_list.remove(exercise)
                subject_list.insert(index_2 + 1, exercise)
            elif exercise_two in subject_list:
                subject_list[index_1], subject_list[index_2] = subject_list[index_2], subject_list[index_1]
                subject_list.remove(exercise_two)
                subject_list.insert(index_1 + 1, exercise_two)
            else:
                subject_list[index_1], subject_list[index_2] = subject_list[index_2], subject_list[index_1]

    elif command == "Exercise":
        if title not in subject_list:
            if exercise not in subject_list:
                subject_list.append(title)
                subject_list.append(exercise)
        else:
            if exercise not in subject_list:
                index_1 = subject_list.index(title)
                subject_list.insert(index_1 + 1, exercise)

    next_command = input()

for n in range(len(subject_list)):
    print(f"{n + 1}.{subject_list[n]}")


a = """
Arrays, Lists, Methods
Swap:Arrays:Methods
Exercise:Databases
Swap:Lists:Databases
Insert:Arrays:0
course start
"""
