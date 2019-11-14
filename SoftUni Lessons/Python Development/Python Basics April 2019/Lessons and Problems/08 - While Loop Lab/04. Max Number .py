num = int(input())

counter = 0
checker = -99999999999999999999999999999999999999999
num2 = 0

while num != counter:
    num2 = int(input())
    if num2 > checker:
        checker = num2
    counter += 1

print(checker)
