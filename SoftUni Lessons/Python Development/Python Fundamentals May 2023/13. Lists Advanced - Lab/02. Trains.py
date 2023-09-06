def trains():
    wagons_count = int(input())
    train = [0] * wagons_count

    while True:
        command = input().split(' ')
        if command[0] == 'End':
            print(train)
            break
        elif command[0] == 'add':
            train[-1] += int(command[1])
        elif command[0] == 'insert':
            train[int(command[1])] += int(command[2])
        elif command[0] == 'leave':
            train[int(command[1])] -= int(command[2])


if __name__ == '__main__':
    trains()
    