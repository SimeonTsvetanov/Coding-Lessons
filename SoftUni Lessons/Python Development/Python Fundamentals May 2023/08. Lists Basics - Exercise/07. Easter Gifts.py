gifts = [g for g in input().split()]

while True:
    command = input().split(' ')

    if command[0] == "No" and command[1] == "Money":
        break

    elif command[0] == "OutOfStock":
        while command[1] in gifts:
            gifts[gifts.index(command[1])] = None

    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

print(' '.join(list(filter(lambda gift: gift, gifts))))
