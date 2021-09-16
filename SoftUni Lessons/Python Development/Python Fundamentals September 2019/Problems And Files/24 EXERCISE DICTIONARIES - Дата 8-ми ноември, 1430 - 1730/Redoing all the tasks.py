def count_chars_in_a_string():
    string = input()
    dictionary = {char: string.count(char) for char in string if char != " "}
    for char, count in dictionary.items():
        print(f"{char} -> {count}")


def a_miner_task():
    resources = {}

    while True:
        resource = input()
        if resource == "stop":
            break
        quantity = int(input())

        if resource in resources.keys():
            resources[resource] += quantity
        else:
            resources[resource] = quantity

    print_it = {print(f"{resource} -> {quantity}") for resource, quantity in resources.items()}


def capitals_task():
    countries = input().split(", ")
    capitals = input().split(", ")
    dictionary = {countries[index]: capitals[index] for index in range(len(countries))}
    print_it = {print(f"{country} -> {capital}") for country, capital in dictionary.items()}


def phonebook_task():
    phonebook = {}

    while True:
        command = input().split("-")
        if len(command) == 1:
            for each_time in range(int(command[0])):
                name = input()
                if name in phonebook.keys():
                    print(f"{name} -> {phonebook[name]}")
                else:
                    print(f"Contact {name} does not exist.")
            break
        phonebook[command[0]] = command[1]


def legendary_farming():
    key_materials = {"shards": 0, "fragments": 0, "motes": 0}
    other_materials = {}

    obtained_item = None

    while True:
        if obtained_item:
            break

        new_materials = input().split(" ")
        for index in range(0, len(new_materials), 2):
            count = int(new_materials[index])
            material = new_materials[index + 1].lower()

            if material in ["shards", "fragments", "motes"]:
                if material in key_materials.keys():
                    key_materials[material] += count
                else:
                    key_materials[material] = count

                if key_materials["shards"] >= 250:
                    obtained_item = "Shadowmourne"
                    key_materials["shards"] -= 250
                    break
                elif key_materials["fragments"] >= 250:
                    key_materials["fragments"] -= 250
                    obtained_item = "Valanyr"
                    break
                elif key_materials["motes"] >= 250:
                    key_materials["motes"] -= 250
                    obtained_item = "Dragonwrath"
                    break
            else:
                if material in other_materials.keys():
                    other_materials[material] += count
                else:
                    other_materials[material] = count

    print(f"{obtained_item} obtained!")
    for key_material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
        print(f"{key_material}: {quantity}")
    for other_material, quantity in sorted(other_materials.items(), key=lambda x: (x[0])):
        print(f"{other_material}: {quantity}")


def orders():
    # like products = {"product_name": ["price", quantity]}

    products = {}
    while True:
        command = input().split(" ")
        if command[0] == "buy":
            break
        product = command[0]
        price = float(command[1])
        quantity = int(command[2])

        if product not in products.keys():
            products[product] = [price, quantity]
        else:
            products[product][0] = price
            products[product][1] += quantity

    print_it = {print(f"{product} -> {(values[0] * values[1]):.2f}") for product, values in products.items()}


def softuni_parking():
    parking = {}

    for each_time in range(int(input())):
        command = input().split(" ")
        if command[0] == "register":
            if command[1] in parking.keys():
                print(f"ERROR: already registered with plate number {parking[command[1]]}")
            else:
                parking[command[1]] = command[2]
                print(f"{command[1]} registered {command[2]} successfully")
        elif command[0] == "unregister":
            if command[1] not in parking.keys():
                print(f"ERROR: user {command[1]} not found")
            else:
                del parking[command[1]]
                print(f"{command[1]} unregistered successfully")

    print_it = {print(f"{name} => {number}") for name, number in parking.items()}


def courses_task():
    courses = {}

    while True:
        command = input().split(" : ")
        if command[0] == "end":
            break
        course, name = command
        if course not in courses.keys():
            courses[course] = [name]
        else:
            courses[course].append(name)

    for course, students in sorted(courses.items(), key=lambda x: (-len(x[1]))):
        print(f"{course}: {len(students)}")
        for student in sorted(students):
            print(f"-- {student}")


def student_academy():
    students = {}

    for each_time in range(int(input())):
        student = input()
        grade = float(input())

        if student not in students.keys():
            students[student] = []
            students[student].append(grade)
        else:
            students[student].append(grade)

    for student, grades in students.items():
        average_grade = sum(grades) / len(grades)
        students[student] = average_grade

    for student, grade in sorted(students.items(), key=lambda x: -x[1]):
        if grade >= 4.5:
            print(f"{student} -> {grade:.2f}")


def company_users():
    companies = {}

    while True:
        command = input().split(" -> ")
        if command[0] == "End":
            break
        company = command[0]
        employee_id = command[1]

        if company not in companies.keys():
            companies[company] = []
        if employee_id not in companies[company]:
            companies[company].append(employee_id)

    for company, employees in sorted(companies.items(), key=lambda x: x[0]):
        print(f"{company}")
        for employee in employees:
            print(f"-- {employee}")


if __name__ == '__main__':
    # count_chars_in_a_string()
    # a_miner_task()
    # capitals_task()
    # phonebook_task()
    # legendary_farming()
    # orders()
    # softuni_parking()
    # courses_task()
    # student_academy()
    # company_users()
    # The last two tasks are to long for me to solve now. 