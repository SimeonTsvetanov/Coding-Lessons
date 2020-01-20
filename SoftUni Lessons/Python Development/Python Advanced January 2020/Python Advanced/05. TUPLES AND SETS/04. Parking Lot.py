car_lot = []

while True:
    command = input()
    if command == "END":
        break
    direction, reg = command.split(", ")
    if direction == "IN":
        if reg not in car_lot:
            car_lot.append(reg)
    elif direction == "OUT":
        if reg in car_lot:
            car_lot.remove(reg)

if car_lot:
    [print(reg) for reg in car_lot]
else:
    print(f"Parking Lot is Empty")

