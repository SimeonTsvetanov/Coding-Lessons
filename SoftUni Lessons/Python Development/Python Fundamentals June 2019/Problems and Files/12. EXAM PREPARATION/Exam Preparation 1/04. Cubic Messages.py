# \d+(?<message>[a-zA-Z]+)
# това е регекса

while True:
    coded_line = input()
    if coded_line == "Over!":
        break
    key = int(input())

    counter_for_numbers = 0
    counter_for_letters = 0
    if_only_digits = True
    for symbol in coded_line:

        if symbol.isdigit():
            counter_for_numbers += 1
            if_only_digits = True






