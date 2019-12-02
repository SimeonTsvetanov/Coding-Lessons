"""
Technology Fundamentals Final Exam - 14 April 2019 Group II
link: https://judge.softuni.bg/Contests/Practice/Index/1594#1
Name: 02. Practice Sessions
"""
roads = {}

while True:
    command = input().split("->")
    if command[0] == "END":
        break

    elif command[0] == "Add":
        add_road = command[1]
        add_racer = command[2]
        if add_road not in roads:
            roads[add_road] = [add_racer]
        elif add_road in roads:
            roads[add_road] += [add_racer]

    elif command[0] == "Move":
        current_road = command[1]
        racer_to_move = command[2]
        next_road = command[3]
        if racer_to_move in roads[current_road]:
            roads[current_road].remove(racer_to_move)
            roads[next_road].append(racer_to_move)

    elif command[0] == "Close":
        road_to_close = command[1]
        if road_to_close in roads:
            del roads[road_to_close]

print(f"Practice sessions:")

for road, racers in sorted(roads.items(), key=lambda x: (-len(x[1]), x[0])):
    print(road)
    for racer in racers:
        print(f"++{racer}")

