state_integers = [int(item) for item in input().split()]
command_integers = [int(item) for item in input().split()]


for command in command_integers:
    if command % 2 == 0:
        state_integers = [int(x * abs(command)) if x % 2 == 0 else x for x in state_integers]
    elif command % 2 != 0:
        state_integers = [int(x // abs(command)) if x % 2 != 0 else x for x in state_integers]
    if command > 0:
        state_integers = [int(x + command) if x > 0 else x for x in state_integers]
    elif command < 0:
        state_integers = [int(x + command) if x < 0 else x for x in state_integers]

print(state_integers)
