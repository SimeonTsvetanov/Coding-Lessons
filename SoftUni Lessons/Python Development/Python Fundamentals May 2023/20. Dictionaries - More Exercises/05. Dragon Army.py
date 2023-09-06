dragons = {}

for each_time in range(int(input())):

    c = input().split(' ')

    d_type = c[0]
    name = c[1]
    damage = int(c[2]) if c[2].isdigit() else 45
    health = int(c[3]) if c[3].isdigit() else 250
    armor = int(c[4]) if c[4].isdigit() else 10

    if d_type not in dragons:
        dragons[d_type] = {}

    dragons[d_type][name] = {'damage': damage, 'health': health, 'armor': armor}


for d_type, c_dragons in dragons.items():
    d = [c_dragons[d]['damage'] for d in c_dragons]
    h = [c_dragons[d]['health'] for d in c_dragons]
    a = [c_dragons[d]['armor'] for d in c_dragons]
    print(f"{d_type}::({(sum(d) / len(d)):.2f}/{(sum(h) / len(h)):.2f}/{(sum(a) / len(a)):.2f})")
    for dragon, stats in sorted(c_dragons.items()):
        print(f"-{dragon} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
