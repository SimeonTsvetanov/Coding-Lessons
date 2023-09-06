year = int(input())

while 'I say so':
    year += 1
    if len(list(set(str(year)))) == len(str(year)):
        print(year)
        break
