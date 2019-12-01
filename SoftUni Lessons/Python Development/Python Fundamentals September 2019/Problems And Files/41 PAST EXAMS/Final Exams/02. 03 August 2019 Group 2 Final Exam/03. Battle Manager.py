"""
Programming Fundamentals Final Exam - 03 August 2019 Group 2
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1749#2
Name: Battle Manager
"""
people = {}

while True:
    command = input().split(":")
    if command[0] == "Results":
        break

    elif command[0] == "Add":
        person_name = command[1]
        health = int(command[2])
        energy = int(command[3])
        if person_name not in people:
            people[person_name] = [health, energy]
        elif person_name in people:
            people[person_name][0] += health

    elif command[0] == "Attack":
        attacker = command[1]
        defender = command[2]
        damage = int(command[3])
        if attacker in people and defender in people:
            people[defender][0] -= damage
            if people[defender][0] <= 0:
                print(f"{defender} was disqualified!")
                del people[defender]
            people[attacker][1] -= 1
            if people[attacker][1] <= 0:
                print(f"{attacker} was disqualified!")
                del people[attacker]

    elif command[0] == "Delete":
        name_to_delete = command[1]
        if name_to_delete == "All":
            people.clear()
        elif name_to_delete in people:
            del people[name_to_delete]

print(f"People count: {len(people)}")

for person, values in sorted(people.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{person} - {values[0]} - {values[1]}")
