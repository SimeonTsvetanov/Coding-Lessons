for each_time in range(int(input())):
    string = input()
    if (',' not in string) and ('.' not in string) and ('_' not in string):
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
