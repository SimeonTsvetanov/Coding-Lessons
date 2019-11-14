money_guest_player = int(input())

command = None

total = 0
people = 0

while not(command == "The restaurant is full"):
    command = input()
    if command == "The restaurant is full":
        break
    group = int(command)
    if group < 5:
        total += 100 * group
    else:
        total += 70 * group
    people += group

if total >= money_guest_player:
    print(f"You have {people} guests and {abs(total - money_guest_player)} leva left.")
else:
    print(f"You have {people} guests and {total} leva income, but no singer.")
