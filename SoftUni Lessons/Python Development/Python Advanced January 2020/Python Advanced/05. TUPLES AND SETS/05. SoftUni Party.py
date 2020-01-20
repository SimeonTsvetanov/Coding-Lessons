regular = []
vip = []

while True:
    reservation = input()
    if reservation == "PARTY":
        break
    if reservation[0].isdigit():
        vip.append(reservation)
    else:
        regular.append(reservation)

while True:
    reservation = input()
    if reservation == "END":
        break
    if reservation in vip:
        vip.remove(reservation)
    elif reservation in regular:
        regular.remove(reservation)

print(len(regular) + len(vip))
for reservation in vip:
    print(reservation)
for reservation in regular:
    print(reservation)
