from collections import deque

waves_trojan_warriors = int(input())
plates_spartan_defence = deque([int(x) for x in input().split()])

wave_trojan_warriors = []

for wave in range(1, waves_trojan_warriors + 1):
    if not plates_spartan_defence:
        break

    wave_trojan_warriors = [int(y) for y in input().split()]

    if wave % 3 == 0:
        spartan_plates_extra_plate = int(input())
        plates_spartan_defence.append(spartan_plates_extra_plate)

    while plates_spartan_defence and wave_trojan_warriors:
        trojan_warrior = wave_trojan_warriors.pop()
        spartan_plate = plates_spartan_defence.popleft()

        if trojan_warrior > spartan_plate:
            wave_trojan_warriors.append(trojan_warrior - spartan_plate)
        elif spartan_plate > trojan_warrior:
            plates_spartan_defence.appendleft(spartan_plate - trojan_warrior)

if not plates_spartan_defence:
    print(f"The Trojans successfully destroyed the Spartan defense.")
    print(f"Warriors left: {', '.join(str(warrior) for warrior in wave_trojan_warriors[::-1])}")
else:
    print(f"The Spartans successfully repulsed the Trojan attack.")
    print(f"Plates left: {', '.join(str(plate) for plate in plates_spartan_defence)}")
