needed_money = int(input())
collected_money = 0
command = None

counter = 0
collected_from_cash = 0
collected_from_card = 0
times_with_cash = 0
times_with_card = 0

while True:
    if collected_money >= needed_money:
        break
    command = input()
    if command == "End":
        break
    counter += 1
    if counter % 2 != 0:
        if int(command) > 100:
            print(f"Error in transaction!")
            continue
        else:
            print(f"Product sold!")
            collected_money += int(command)
            collected_from_cash += int(command)
            times_with_cash +=1
    else:
        if int(command) < 10:
            print(f"Error in transaction!")
            continue
        else:
            print(f"Product sold!")
            collected_money += int(command)
            collected_from_card += int(command)
            times_with_card += 1

if command == "End" and collected_money < needed_money:
    print(f"Failed to collect required money for charity.")
else:
    print(f"Average CS: {(collected_from_cash / times_with_cash):.2f}")
    print(f"Average CC: {(collected_from_card / times_with_card):.2f}")


