count_bottles = int(input())
volume = count_bottles * 750

count_dishes = 0
count_pots = 0

command = None
counter = 0

while True:
    if volume < 0:
        break
    command = input()
    if command == "End":
        break
    if volume - int(command) < 0:
        break
    counter += 1
    if counter == 3:
        volume -= int(command) * 15
        count_pots += int(command)
        counter = 0
    else:
        volume -= int(command) * 5
        count_dishes += int(command)

if command == "End" and volume >= 0:
    print(f"Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {volume} ml.")
else:
    print(f"Not enough detergent, {abs(volume)} ml. more necessary!")
