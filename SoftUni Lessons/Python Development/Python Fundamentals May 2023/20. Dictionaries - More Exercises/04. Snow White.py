dwarfs = []

while True:
    command = input().split(' <:> ')

    if command[0] == 'Once upon a time':
        break

    name = command[0]
    color = command[1]
    power = int(command[2])

    present_dwarf = [d for d in dwarfs if (d['name'] == name) and (d['color'] == color)]

    if not present_dwarf:
        dwarfs.append({'name': name, 'color': color, 'power': power})
    else:
        present_dwarf[0]['power'] = max(present_dwarf[0]['power'], power)

for dwarf in sorted(dwarfs, key=lambda x: (-x['power'], -len([d for d in dwarfs if d['color'] == x['color']]))):
    print(f"({dwarf['color']}) {dwarf['name']} <-> {dwarf['power']}")
