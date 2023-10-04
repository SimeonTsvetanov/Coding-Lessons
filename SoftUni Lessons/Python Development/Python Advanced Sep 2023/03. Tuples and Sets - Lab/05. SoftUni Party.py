regular = set()
vip = set()

for _ in range(int(input())):
    guest = input()
    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

while 'tikvichkite sa bezvkusni':
    liaison = input()
    if liaison == 'END':
        break
    if liaison[0].isdigit() and liaison in vip:
        vip.remove(liaison)
    elif liaison in regular:
        regular.remove(liaison)

print(len(regular) + len(vip))
[print(guest) for guest in sorted(list(vip))]
[print(guest) for guest in sorted(list(regular))]

