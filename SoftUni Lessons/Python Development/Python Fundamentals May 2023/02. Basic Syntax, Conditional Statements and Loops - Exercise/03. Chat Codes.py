for _ in range(int(input())):
    x = int(input())
    if x == 88:
        print('Hello')
    elif x == 86:
        print('How are you?')
    elif (x not in [86, 88]) and x < 88:
        print("GREAT!")
    elif x > 88:
        print('Bye.')
