money_for_guest = int(input())

command = None
total_people = 0
total_income = 0

while True:
    command = input()
    if command == "The restaurant is full":
        break
    count_group = int(command)
    total_people += count_group
    if count_group < 5:
        total_income += 100 * count_group
    else:
        total_income += 70 * count_group

if total_income >= money_for_guest:
    print(f"You have {total_people} guests and {(total_income - money_for_guest)} leva left.")
else:
    print(f"You have {total_people} guests and {total_income} leva income, but no singer.")
