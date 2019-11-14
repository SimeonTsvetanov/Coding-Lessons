import math

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_person_height = float(input())

ship_size = ship_width * ship_length * ship_height
room_size = (average_person_height + 0.4) * 2 * 2

count = math.floor(ship_size / room_size)

if 3 <= count <= 10:
    print(f"The spacecraft holds {count} astronauts.")
elif count < 3:
    print(f"The spacecraft is too small.")
elif count > 10:
    print(f"The spacecraft is too big.")
