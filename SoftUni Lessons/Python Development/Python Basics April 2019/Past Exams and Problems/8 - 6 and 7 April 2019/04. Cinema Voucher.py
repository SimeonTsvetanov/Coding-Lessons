vch_amount = int(input())

command = None
current_price = 0
count_movies = 0
count_others = 0

while command != "End":
    command = input()
    if command == "End":
        break
    name = len(command)
    if name > 8:
        current_price = ord(command[0]) + ord(command[1])
        if vch_amount - current_price >= 0:
            vch_amount -= current_price
            count_movies += 1
        else:
            break
    elif name <= 8:
        current_price = ord(command[0])
        if vch_amount - current_price >= 0:
            vch_amount -= current_price
            count_others += 1
        else:
            break

print(count_movies)
print(count_others)
