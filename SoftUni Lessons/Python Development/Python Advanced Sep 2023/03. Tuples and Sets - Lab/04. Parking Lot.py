parking = set()

for _ in range(int(input())):
    direction, plate = input().split(', ')
    parking.remove(plate) if (direction == 'OUT' and plate in parking) else parking.add(plate)

print('\n'.join(list(parking))) if parking else print('Parking Lot is Empty')
